from django.contrib import admin
from .models import (AuthorModel, BookModel, FineModel, GenreModel,
                     LibraryStaffModel, LoanModel)
from datetime import datetime

class LoanDateFilter(admin.SimpleListFilter):
    title = 'Fecha de préstamo'
    parameter_name = 'loan_date'

    def lookups(self, request, model_admin):
        return [
            ('today', 'Hoy'),
            ('yesterday', 'Ayer'),
            ('last_7_days', 'Últimos 7 días'),
            ('this_month', 'Este mes'),
        ]

    def queryset(self, request, queryset):
        from datetime import datetime, timedelta

        today = datetime.today().date()
        if self.value() == 'today':
            return queryset.filter(loan_book__start_date=today)
        if self.value() == 'yesterday':
            yesterday = today - timedelta(days=1)
            return queryset.filter(loan_book__start_date=yesterday)
        if self.value() == 'last_7_days':
            last_7_days = today - timedelta(days=7)
            return queryset.filter(loan_book__start_date__gte=last_7_days)
        if self.value() == 'this_month':
            return queryset.filter(loan_book__start_date__month=today.month)

        return queryset

@admin.register(BookModel)
class BookModelAdmin(admin.ModelAdmin):
    filter_horizontal = ['genre', 'author']
    list_display = ['title', 'get_total_loans', 'is_available']
    list_filter = ['is_active', 'is_available', LoanDateFilter]
    actions = ['make_available', 'make_unavailable']
    search_fields = ['title', 'loan_date']

    def get_total_loans(self, obj):
        return LoanModel.objects.filter(book=obj).count()
    
    def get_loans_on_date(self, obj):
        date_str = self.request.GET.get('loan_date')
        
        if date_str:
            try:
                specific_date = datetime.strptime(date_str, '%Y-%m-%d').date()
                loans_on_date = LoanModel.objects.filter(book=obj, start_date=specific_date).count()
            except ValueError:
                loans_on_date = 0
        else:
            loans_on_date = 0
        
        return loans_on_date

    def make_available(self, request, queryset):
        queryset.update(is_available=True)

    def make_unavailable(self, request, queryset):
        queryset.update(is_available=False)

    get_total_loans.short_description = 'Total de préstamos realizados'
    make_unavailable.short_description = "Marcar como no disponible"
    make_available.short_description = "Marcar como disponible"
    
    def parse_date(self, date_str):
        """
        Intenta convertir una cadena de texto a una fecha utilizando múltiples formatos.
        """
        date_formats = ['%Y-%m-%d', '%d-%m-%Y', '%Y/%m/%d', '%d/%m/%Y']
        for date_format in date_formats:
            try:
                return datetime.strptime(date_str, date_format).date()
            except ValueError:
                continue
        return None

    def get_search_results(self, request, queryset, search_term):
        """
        Sobrescribir el método get_search_results para filtrar por fecha de préstamo.
        """
        # Guardar la solicitud para usarla en get_loans_on_date
        self.request = request

        specific_date = self.parse_date(search_term)
        if specific_date:
            # Filtrar los libros que tienen préstamos en la fecha especificada
            queryset = queryset.filter(loan_book__start_date=specific_date).distinct()
            use_distinct = True
        else:
            # Si no es una fecha, usar la lógica de búsqueda predeterminada
            queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        
        return queryset, use_distinct
    
    def changelist_view(self, request, extra_context=None):
        self.request = request
        return super().changelist_view(request, extra_context)


@admin.register(LoanModel)
class LoanModelAdmin(admin.ModelAdmin):
    filter_horizontal = ['book']
    list_display = ['user', 'start_date', 'end_date', 'status', 'return_date']

@admin.register(LibraryStaffModel)
class LibraryStaffModelAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'is_chief_librarian',
        'get_books_loaned',
        'get_total_loans'
    ]

    readonly_fields = (
        'created',
        'updated',
        'get_books_loaned',
        'get_total_loans',
        'get_loans',
        'get_books_loan'
    )

    fieldsets = (
        (
            ('Información de usuario'), {
                'fields': (
                    'user',
                    'is_chief_librarian',
                    'department',
                    'superior'
                )
            }
        ),
        (
            ('Préstamos'), {
                'fields': (
                    'get_books_loaned',
                    'get_loans',
                    'get_total_loans',
                    'get_books_loan'
                )
            }
        )
    )

    def get_books_loaned(self, obj):
        loans = LoanModel.objects.filter(user=obj.user)
        books = [loan.book.all() for loan in loans]
        return ', '.join([book.title for sublist in books for book in sublist])
    
    def get_books_loan(self, obj):
        loans = LoanModel.objects.filter(user=obj.user, status='active')
        books = [loan.book.all() for loan in loans]
        return ', '.join([book.title for sublist in books for book in sublist])

    def get_total_loans(self, obj):
        return LoanModel.objects.filter(user=obj.user).count()
    
    def get_loans(self, obj):
        loans = LoanModel.objects.filter(user=obj.user)
        return ', '.join([str(loan) for loan in loans])

    get_books_loaned.short_description = 'Historico de libros prestados'
    get_total_loans.short_description = 'Total de préstamos realizados'
    get_books_loan.short_description = 'Libros prestados actualmente'
    get_loans.short_description = 'Préstamos'

@admin.register(FineModel)
class FineModelAdmin(admin.ModelAdmin):
    list_display = ['loan', 'date', 'amount',
                    'paid', 'return_date', 'get_books']

    def get_books(self, obj):
        books = obj.loan.book.all()
        return ', '.join([book.title for book in books])

    get_books.short_description = "Libros"


admin.site.register([GenreModel, AuthorModel])
