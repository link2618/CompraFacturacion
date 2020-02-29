# Generated by Django 2.2 on 2020-02-27 22:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0005_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='uc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario Crea'),
        ),
        migrations.AlterField(
            model_name='marca',
            name='uc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario Crea'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='uc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario Crea'),
        ),
        migrations.AlterField(
            model_name='subcategoria',
            name='uc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario Crea'),
        ),
        migrations.AlterField(
            model_name='unidadmedida',
            name='uc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario Crea'),
        ),
    ]