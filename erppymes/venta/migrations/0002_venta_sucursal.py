# Generated by Django 2.2.4 on 2021-07-31 14:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seguridad', '0002_empleado_group'),
        ('venta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='sucursal',
            field=models.ForeignKey(default=datetime.date, on_delete=django.db.models.deletion.PROTECT, to='seguridad.Sucursal'),
            preserve_default=False,
        ),
    ]
