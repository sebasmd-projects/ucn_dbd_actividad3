import random
from datetime import timedelta
from django.utils import timezone
from apps.project.library.models import AuthorModel, GenreModel, BookModel
from apps.project.users.models import Career, Department
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    help = "LLenar los datos de forma automática"
    
    def handle(self, *arg, **options):
        
        authors = ['Gabriel García Márquez', 'Jane Austen', 'Leo Tolstoy', 'Stephen King', 'J.K. Rowling']
        for author_name in authors:
            AuthorModel.objects.get_or_create(name=author_name)
            
        genres = ['Misterio', 'Romance', 'Ciencia ficción']
        for genre_name in genres:
            GenreModel.objects.get_or_create(name=genre_name)
            
        for i in range(20):
            title = f'Título {i}'
            author = random.choice(AuthorModel.objects.all())
            genre = random.choice(GenreModel.objects.all())
            publication_date = timezone.now() - timedelta(days=random.randint(100, 365)*30)
            
            book = BookModel.objects.create(title=title, publication_date=publication_date)
            book.author.set([author])
            book.genre.set([genre])
            
        careers = ['Ingeniería de Sistemas', 'Ingeniería Civil', 'Administración de Empresas', 'Derecho', 'Medicina']
        for career_name in careers:
            Career.objects.get_or_create(name=career_name)

        departments = ['Ingeniería', 'Ciencias Sociales', 'Ciencias de la Salud', 'Humanidades']
        for department_name in departments:
            Department.objects.get_or_create(name=department_name)