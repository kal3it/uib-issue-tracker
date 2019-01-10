# Generated by Django 2.1.5 on 2019-01-09 19:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190109_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='assignee',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assignee', to=settings.AUTH_USER_MODEL, verbose_name='Asignado a'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='codename',
            field=models.CharField(max_length=255, verbose_name='Referencia'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='description',
            field=models.TextField(verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='priority',
            field=models.CharField(choices=[('low', 'Baja'), ('middle', 'Media'), ('high', 'Alta'), ('severe', 'Grave'), ('critical', 'Crítica')], max_length=255, verbose_name='Prioridad'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('new', 'Nuevo'), ('assigned', 'Asignado'), ('in-progress', 'En proceso'), ('solved', 'Resuelto')], default='new', editable=False, max_length=255, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='type',
            field=models.CharField(choices=[('issue', 'Incidencia'), ('request', 'Petición'), ('system', 'Sistemas')], max_length=255, verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Última actualización'),
        ),
    ]
