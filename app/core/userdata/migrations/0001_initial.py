# Generated by Django 2.2 on 2020-05-07 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatosUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userDNI', models.CharField(max_length=20)),
                ('fotoUser', models.ImageField(default='user.png', upload_to='', verbose_name='Foto de perfil')),
                ('teleUser', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Datos de Usuario',
                'verbose_name_plural': 'Información',
            },
        ),
        migrations.CreateModel(
            name='HabilUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombHabil', models.CharField(max_length=100)),
                ('DescHabil', models.TextField(max_length=2000, verbose_name='Descripcion de la habilidad')),
            ],
            options={
                'verbose_name': 'Habilidades del Usuario',
                'verbose_name_plural': 'Competencias',
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RoleName', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Perfil de Usuario',
                'verbose_name_plural': 'perfiles',
            },
        ),
        migrations.CreateModel(
            name='Rates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pcrHabil', models.DecimalField(decimal_places=1, max_digits=2)),
                ('udtHabil', models.DateTimeField(auto_now=True)),
                ('idHabil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userdata.HabilUser')),
                ('idUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userdata.DatosUser')),
            ],
            options={
                'verbose_name': 'Nivel de Habilidad',
                'verbose_name_plural': 'Niveles de usuario',
            },
        ),
        migrations.CreateModel(
            name='DetaRoles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addUser', models.DateTimeField(auto_now_add=True)),
                ('udtUser', models.DateTimeField(auto_now=True)),
                ('estaRol', models.CharField(max_length=10)),
                ('idRoles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userdata.Roles', verbose_name='Identificador de Rol')),
                ('idUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userdata.DatosUser')),
            ],
            options={
                'verbose_name': 'Roles de Usuario',
                'verbose_name_plural': 'Roles',
            },
        ),
    ]
