# Generated by Django 2.2.4 on 2021-07-31 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_articulo_sucursal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=19, verbose_name='Precio'),
        ),
    ]
