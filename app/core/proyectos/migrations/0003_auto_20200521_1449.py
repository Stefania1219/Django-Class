# Generated by Django 2.2 on 2020-05-21 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0002_auto_20200521_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyectos',
            name='imgProye',
            field=models.ImageField(max_length=200, upload_to='img/proyectos', verbose_name='Imagen del proyecto'),
        ),
    ]
