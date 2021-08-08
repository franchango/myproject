# Generated by Django 2.2.4 on 2020-08-26 09:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=200, verbose_name='Nombre')),
                ('ruc', models.CharField(default='', max_length=15, verbose_name='cedula')),
                ('direcion', models.CharField(default='', max_length=50, verbose_name='direccion')),
                ('celular', models.CharField(default='', max_length=50, verbose_name='celular')),
                ('image', models.ImageField(default='', upload_to='empresa/%Y/%m/%d/')),
                ('email', models.CharField(default='', max_length=200, verbose_name='Email')),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Grupo de Empresa',
                'verbose_name_plural': 'Grupos de Empresa',
                'ordering': ('nombre', 'nombre'),
            },
        ),
        migrations.CreateModel(
            name='Fotouser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('icono', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
                ('orden', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Módulo',
                'verbose_name_plural': 'Módulos',
                'ordering': ['orden'],
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razonsocial', models.CharField(default='', max_length=200, verbose_name='razonsocial')),
                ('ruc', models.CharField(default='', max_length=15, verbose_name='ruc')),
                ('direcion', models.CharField(default='', max_length=50, verbose_name='direccion')),
                ('celular', models.CharField(default='', max_length=50, verbose_name='celular')),
                ('image', models.ImageField(default='', upload_to='sucursal/%Y/%m/%d/')),
                ('email', models.CharField(default='', max_length=200, verbose_name='Email')),
                ('status', models.BooleanField(default=True)),
                ('canton', models.CharField(default='', max_length=15, verbose_name='Ciudad')),
                ('provincia', models.CharField(default='', max_length=15, verbose_name='provincia')),
                ('sucursal_id', models.IntegerField(default=0)),
                ('elim', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Grupo de Sucursal',
                'verbose_name_plural': 'Grupos de Sucursal',
                'ordering': ('razonsocial', 'razonsocial'),
            },
        ),
        migrations.CreateModel(
            name='ModuloGrupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(blank=True, max_length=200)),
                ('prioridad', models.IntegerField(blank=True, null=True)),
                ('icono', models.CharField(max_length=100)),
                ('grupos', models.ManyToManyField(to='auth.Group')),
                ('modulos', models.ManyToManyField(to='seguridad.Modulo')),
            ],
            options={
                'verbose_name': 'Grupo de Módulos',
                'verbose_name_plural': 'Grupos de Módulos',
                'ordering': ('prioridad', 'nombre'),
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(default='', max_length=15, verbose_name='cedula')),
                ('direcion', models.CharField(default='', max_length=50, verbose_name='direccion')),
                ('celular', models.CharField(default='', max_length=50, verbose_name='celular')),
                ('image', models.ImageField(default='', upload_to='empleado/%Y/%m/%d/')),
                ('fecha', models.DateTimeField(blank=True, default='', verbose_name='Fecha Ingreso')),
                ('status', models.BooleanField(default=True)),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='seguridad.Sucursal')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Grupo de Empleado',
                'verbose_name_plural': 'Grupos de Empleados',
                'ordering': ('id', 'id'),
            },
        ),
    ]
