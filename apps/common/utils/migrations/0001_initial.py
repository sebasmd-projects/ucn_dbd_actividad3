# Generated by Django 4.2.7 on 2024-06-10 17:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RequestLogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, default='es', max_length=50, null=True, verbose_name='idioma')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='creado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='actualizado')),
                ('is_active', models.BooleanField(default=True, verbose_name='esta activo')),
                ('default_order', models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='prioridad')),
                ('requests', models.JSONField(blank=True, default=dict, null=True, verbose_name='peticiones')),
            ],
            options={
                'verbose_name': 'Peticiones',
                'verbose_name_plural': 'Peticiones',
                'db_table': 'apps_common_utils_requestlog',
            },
        ),
    ]
