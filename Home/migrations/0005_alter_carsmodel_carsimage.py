# Generated by Django 4.1.4 on 2022-12-25 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_alter_carsmodel_carssalary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carsmodel',
            name='CarsImage',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
