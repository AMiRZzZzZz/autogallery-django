# Generated by Django 4.1.4 on 2022-12-27 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0010_alter_carsmodel_carsimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singlecarmodel',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Home.carsmodel'),
        ),
    ]