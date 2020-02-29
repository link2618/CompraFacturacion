# Generated by Django 2.2 on 2020-02-27 22:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inv', '0006_auto_20200227_1734'),
        ('cmp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='uc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario Crea'),
        ),
        migrations.CreateModel(
            name='ComprasEnc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fc', models.DateTimeField(auto_now_add=True, verbose_name='Fecha De Creación')),
                ('fm', models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('um', models.IntegerField(blank=True, null=True, verbose_name='Usuario Modifica')),
                ('fecha_compra', models.DateField(blank=True, null=True, verbose_name='Fecha de compra')),
                ('observacion', models.TextField(blank=True, null=True, verbose_name='Observación')),
                ('no_factura', models.CharField(max_length=100, verbose_name='Numero de Factura')),
                ('fecha_factura', models.DateField(verbose_name='Fecha de factura')),
                ('sub_total', models.FloatField(default=0, verbose_name='Sub Total')),
                ('descuento', models.FloatField(default=0, verbose_name='Descuento')),
                ('total', models.FloatField(default=0, verbose_name='Total')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmp.Proveedor')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario Crea')),
            ],
            options={
                'verbose_name': 'Encabezado Compra',
                'verbose_name_plural': 'Encabezado Compras',
            },
        ),
        migrations.CreateModel(
            name='CompraDet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fc', models.DateTimeField(auto_now_add=True, verbose_name='Fecha De Creación')),
                ('fm', models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('um', models.IntegerField(blank=True, null=True, verbose_name='Usuario Modifica')),
                ('cantidad', models.BigIntegerField(default=0, verbose_name='Cantidad')),
                ('precio_prv', models.FloatField(default=0, verbose_name='Precio Proveedor')),
                ('sub_total', models.FloatField(default=0, verbose_name='Sub Total')),
                ('descuento', models.FloatField(default=0, verbose_name='Descuento')),
                ('total', models.FloatField(default=0, verbose_name='Total')),
                ('costo', models.FloatField(default=0, verbose_name='Costo')),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmp.ComprasEnc')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inv.Producto')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario Crea')),
            ],
            options={
                'verbose_name': 'Detalle Compra',
                'verbose_name_plural': 'Detalles Compas',
            },
        ),
    ]
