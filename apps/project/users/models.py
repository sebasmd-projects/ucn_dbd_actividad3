import uuid
from datetime import date

from auditlog.registry import auditlog
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from app_core.settings_config import get_app_from_path

TimeStampedModel = get_app_from_path(
    f'{settings.UTILS_PATH}.models.TimeStampedModel'
)


class Career(TimeStampedModel):
    name = models.CharField(_('nombre'), max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'apps_project_career'
        verbose_name = _('Carrerra')
        verbose_name_plural = _('Carrerra')


class Department(TimeStampedModel):
    name = models.CharField(_('nombre'), max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'apps_project_department'
        verbose_name = _('Departmento')
        verbose_name_plural = _('Departmentos')


class UserModel(TimeStampedModel, AbstractUser):
    id = models.UUIDField(
        'ID',
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        serialize=False,
        editable=False
    )

    is_teacher = models.BooleanField(
        _("es docente"),
        default=False
    )
    
    is_student = models.BooleanField(
        _("es estudiante"),
        default=False
    )

    identification_card = models.CharField(
        'carnet',
        max_length=100,
    )

    cell_phone = models.CharField(
        _('celular'),
        max_length=15,
        null=True,
        blank=True
    )

    birthday = models.DateField(
        _('fecha de nacimiento'),
        default=date.today,
        blank=True,
        null=True
    )

    address = models.TextField(
        _('dirección'),
        blank=True,
        null=True
    )

    career = models.ForeignKey(
        Career,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='students'
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='teachers'
    )

    REQUIRED_FIELDS = [
        'email',
        'first_name',
        'last_name'
    ]

    def get_age(self):
        return date.today().year - self.birthday.year - (
            (date.today().month, date.today().day) < (
                self.birthday.month, self.birthday.day)
        )

    def save(self, *args, **kwargs):
        self.first_name = self.first_name.title()
        self.last_name = self.last_name.title()
        self.username = self.username.lower()

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.get_full_name()}"

    class Meta:
        db_table = 'apps_project_common_user'
        verbose_name = _('Usuario')
        verbose_name_plural = _('Usuarios')


auditlog.register(
    UserModel,
    serialize_data=True
)
