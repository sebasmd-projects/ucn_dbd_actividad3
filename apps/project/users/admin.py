from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportActionModelAdmin

from apps.project.library.models import FineModel, LoanModel

from .models import Career, Department, UserModel


@admin.register(UserModel)
class UserModelAdmin(UserAdmin, ImportExportActionModelAdmin):
    search_fields = (
        'id',
        'username',
        'email',
        'cell_phone',
        'first_name',
        'last_name',
    )

    list_filter = (
        'is_active',
        'is_staff',
        'is_superuser',
        'is_teacher'
    )

    list_display = (
        'get_full_name',
        'get_books_loaned',
        'get_total_fines',
        'username',
        'email',
        'identification_card',
        'cell_phone',
        'is_staff',
        'is_active'
    )

    list_display_links = (
        'get_full_name',
        'username',
        'email',
    )

    ordering = (
        'default_order',
        'created',
        'last_name',
        'first_name',
        'email',
        'username',
    )

    readonly_fields = (
        'created',
        'updated',
        'last_login',
        'get_age',
        'get_books_loaned',
        'get_books_loan',
        'get_loans',
        'get_total_fines',
        'get_fines'
    )

    fieldsets = (
        (
            _('Información de usuario'), {
                'fields': (
                    'username',
                    'password',
                    'identification_card',
                    'career',
                    'department',
                    'is_student',
                    'is_teacher',
                )
            }
        ),
        (
            _('Préstamos'), {
                'fields': (
                    'get_books_loaned',
                    'get_books_loan',
                    'get_loans'
                )
            }
        ),
        (
            _('Multas'), {
                'fields': (
                    'get_total_fines',
                    'get_fines'
                )
            }
        ),
        (
            _('Información personal'), {
                'fields': (
                    'first_name',
                    'last_name',
                    'address',
                    'email',
                    'cell_phone',
                    'birthday',
                    'get_age',
                )
            }
        ),
        (
            _('Permisos'), {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions'
                )
            }
        ),
        (
            _('Fechas'), {
                'fields': (
                    'last_login',
                    'created',
                    'updated'
                )
            }
        ),
        (
            _('Orden por defecto'), {
                'fields': (
                    'default_order',
                )
            }
        )
    )

    def get_age(self, obj):
        return obj.get_age()

    def get_full_name(self, obj):
        return obj.get_full_name()

    def get_books_loaned(self, obj):
        loans = LoanModel.objects.filter(user=obj)
        books = [loan.book.all() for loan in loans]
        return ', '.join([book.title for sublist in books for book in sublist])

    def get_books_loan(self, obj):
        loans = LoanModel.objects.filter(user=obj, status='active')
        books = [loan.book.all() for loan in loans]
        return ', '.join([book.title for sublist in books for book in sublist])

    def get_loans(self, obj):
        loans = LoanModel.objects.filter(user=obj)
        return ', '.join([str(loan) for loan in loans])

    def get_total_fines(self, obj):
        return FineModel.objects.filter(loan__user=obj).count() or 0

    def get_fines(self, obj):
        fines = FineModel.objects.filter(loan__user=obj)
        return ', '.join([str(fine) for fine in fines])

    get_full_name.short_description = _('Nombres completos')

    get_age.short_description = _('Edad')

    get_books_loaned.short_description = 'Historico de libros prestados'

    get_books_loan.short_description = 'Libros prestados actualmente'

    get_total_fines.short_description = 'Total de multas'

    get_loans.short_description = "Préstamos"
    
    get_fines.short_description = "Multas"


admin.site.register(Department)
admin.site.register(Career)
