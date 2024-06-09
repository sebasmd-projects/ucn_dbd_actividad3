from django.core.management.base import BaseCommand
from django.utils import timezone
from apps.project.library.models import LoanModel

class Command(BaseCommand):
    help = 'Verifica y actualiza el estado de los objetos según la fecha'

    def handle(self, *args, **kwargs):
        today_date = timezone.now()
        objects_to_verify = LoanModel.objects.filter(end_date__lt=today_date, status='active')
        for object in objects_to_verify:
            object.status = 'overdue'
            object.save()
        self.stdout.write(self.style.SUCCESS('Los prestamos han sido actualizados correctamente.'))