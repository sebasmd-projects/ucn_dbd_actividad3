# Generated by Django 4.2.7 on 2024-06-09 17:49

import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, default='es', max_length=50, null=True, verbose_name='idioma')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='creado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='actualizado')),
                ('is_active', models.BooleanField(default=True, verbose_name='esta activo')),
                ('default_order', models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='prioridad')),
                ('name', models.CharField(max_length=100, verbose_name='nombre')),
            ],
            options={
                'verbose_name': 'Carrerra',
                'verbose_name_plural': 'Carrerra',
                'db_table': 'apps_project_career',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, default='es', max_length=50, null=True, verbose_name='idioma')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='creado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='actualizado')),
                ('is_active', models.BooleanField(default=True, verbose_name='esta activo')),
                ('default_order', models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='prioridad')),
                ('name', models.CharField(max_length=100, verbose_name='nombre')),
            ],
            options={
                'verbose_name': 'Departmento',
                'verbose_name_plural': 'Departmentos',
                'db_table': 'apps_project_department',
            },
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('language', models.CharField(blank=True, default='es', max_length=50, null=True, verbose_name='idioma')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='creado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='actualizado')),
                ('is_active', models.BooleanField(default=True, verbose_name='esta activo')),
                ('default_order', models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='prioridad')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('is_teacher', models.BooleanField(default=False, verbose_name='es docente')),
                ('is_student', models.BooleanField(default=False, verbose_name='es estudiante')),
                ('identification_card', models.CharField(max_length=100, verbose_name='carnet')),
                ('cell_phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='celular')),
                ('birthday', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='fecha de nacimiento')),
                ('address', models.TextField(blank=True, null=True, verbose_name='dirección')),
                ('career', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='users.career')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teachers', to='users.department')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'apps_project_common_user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]