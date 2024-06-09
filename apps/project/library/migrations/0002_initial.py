# Generated by Django 4.2.7 on 2024-06-09 17:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('library', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='loanmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loans', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='librarystaffmodel',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='staff', to='users.department'),
        ),
        migrations.AddField(
            model_name='librarystaffmodel',
            name='superior',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subordinates', to='library.librarystaffmodel'),
        ),
        migrations.AddField(
            model_name='librarystaffmodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='staff_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='finemodel',
            name='loan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loan', to='library.loanmodel'),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='author',
            field=models.ManyToManyField(blank=True, related_name='book_author', to='library.authormodel', verbose_name='Autor'),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='genre',
            field=models.ManyToManyField(blank=True, related_name='book_genre', to='library.genremodel', verbose_name='Género'),
        ),
    ]