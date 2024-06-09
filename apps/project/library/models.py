from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

from app_core.settings_config import get_app_from_path

UserModel = get_user_model()

TimeStampedModel = get_app_from_path(
    f'{settings.UTILS_PATH}.models.TimeStampedModel'
)

Department = get_app_from_path(
    'apps.project.users.models.Department'
)


class AuthorModel(TimeStampedModel):
    name = models.CharField(
        _('autor'),
        max_length=250
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'apps_project_author'
        verbose_name = _('Autor')
        verbose_name_plural = _('Autor')


class GenreModel(TimeStampedModel):
    name = models.CharField(
        _('género'),
        max_length=100
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'apps_project_genre'
        verbose_name = _('Género')
        verbose_name_plural = _('Géneros')


class BookModel(TimeStampedModel):
    title = models.CharField(
        _('título'),
        max_length=255
    )

    author = models.ManyToManyField(
        AuthorModel,
        related_name='book_author',
        verbose_name=_('Autor'),
        blank=True
    )

    genre = models.ManyToManyField(
        GenreModel,
        related_name='book_genre',
        verbose_name=_('Género'),
        blank=True
    )

    publication_date = models.DateField(
        _('fecha de publicación'),
        blank=True,
        null=True
    )

    is_available = models.BooleanField(
        _('disponibilidad'),
        default=True
    )

    def __str__(self):
        return f"{self.title} - Disponible: {'Si' if self.is_available else 'No'}"

    class Meta:
        db_table = 'apps_project_book'
        verbose_name = _('Libro')
        verbose_name_plural = _('Libros')


class LibraryStaffModel(TimeStampedModel):
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        related_name='staff_profile'
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='staff'
    )

    is_chief_librarian = models.BooleanField(
        _('es bibliotecario jefe'),
        default=False
    )

    superior = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='subordinates'
    )

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        db_table = 'apps_project_library_staff'
        verbose_name = _('Personal de la biblioteca')
        verbose_name_plural = _('Personal de la biblioteca')


class LoanModel(TimeStampedModel):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='loans'
    )

    book = models.ManyToManyField(
        BookModel,
        related_name='loan_book',
        verbose_name=_('Libros')
    )

    start_date = models.DateField(
        _('fecha de inicio')
    )

    end_date = models.DateField(
        _('fecha de finalización')
    )

    status = models.CharField(
        _('estado'),
        max_length=20,
        choices=[
            ('active', 'Activo'),
            ('overdue', 'Vencido'),
            ('returned', 'Devuelto')
        ],
        default='active'
    )

    return_date = models.DateField(
        _('fecha de devolución'),
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.id} - Préstamo a {self.user.get_full_name()}"

    def save(self, *args, **kwargs):
        if self.status == 'active' and self.end_date < now().date():
            self.status = 'overdue'
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'apps_project_loan'
        verbose_name = _('Prestamo')
        verbose_name_plural = _('Prestamos')


class FineModel(TimeStampedModel):
    loan = models.ForeignKey(
        LoanModel,
        on_delete=models.CASCADE,
        related_name='loan',
        verbose_name='préstamo'
    )

    date = models.DateField(
        _('fecha de inicio de la multa')
    )

    amount = models.DecimalField(
        _('valor de la multa'),
        max_digits=10,
        decimal_places=2,
        default=0
    )

    paid = models.BooleanField(
        _('pagada'),
        default=False
    )

    return_date = models.DateField(
        _('fecha de devolución'),
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Multa a {self.loan.user.get_full_name()} prestamo {self.loan.id}"

    class Meta:
        db_table = 'apps_project_fine'
        verbose_name = _('Multa')
        verbose_name_plural = _('Multas')


@receiver(post_save, sender=FineModel)
def update_loan_status(sender, instance, created, **kwargs):
    if instance.paid and instance.return_date:
        instance.loan.status = 'returned'
        instance.loan.return_date = instance.return_date
        instance.loan.save()


@receiver(post_save, sender=LoanModel)
def create_or_update_fine(sender, instance, created, **kwargs):
    if instance.status == 'active' and instance.end_date < now().date():
        instance.status = 'overdue'

    if instance.status == 'overdue':
        overdue_days = (now().date() - instance.end_date).days
        amount = 10000 + overdue_days * 1000

        fine, fine_created = FineModel.objects.get_or_create(
            loan=instance,
            defaults={'date': now().date(), 'amount': amount}
        )

        if not fine_created:
            fine.date = now().date()
            fine.amount = amount
            fine.save()

    if instance.status == 'returned':
        FineModel.objects.filter(loan=instance).update(
            paid=True, return_date=now().date()
        )


@receiver(m2m_changed, sender=LoanModel.book.through)
def update_books_status(sender, instance, action, **kwargs):
    if action == 'post_add' or action == 'post_remove':
        if instance.status == 'active':
            instance.book.all().update(is_available=False)
        elif instance.status == 'returned':
            instance.book.all().update(is_available=True)