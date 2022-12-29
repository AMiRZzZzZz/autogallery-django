# Generated by Django 4.1.4 on 2022-12-29 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0015_remove_singlecarmodel_car_singlecarmodel_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='carsmodel',
            name='CarsLuggage',
            field=models.IntegerField(choices=[(1, '2'), (2, '3'), (3, '4'), (4, '5')], default=2),
        ),
        migrations.AddField(
            model_name='carsmodel',
            name='CarsMileage',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='carsmodel',
            name='CarsSerial',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='carsmodel',
            name='CarsTransmision',
            field=models.IntegerField(choices=[(1, 'Automatic'), (2, 'Manual')], default=2),
        ),
        migrations.AddField(
            model_name='carsmodel',
            name='Cars_Fuel',
            field=models.IntegerField(choices=[(1, 'gas'), (2, 'Petrol'), (3, 'electric'), (4, 'hybrid(Patrol & gas)'), (5, 'hybrid(Patrol & electric)')], default=3),
        ),
        migrations.AddField(
            model_name='carsmodel',
            name='Cars_Seats',
            field=models.IntegerField(choices=[(1, '2'), (2, '4'), (3, '5')], default=2),
        ),
        migrations.AlterField(
            model_name='carsmodel',
            name='CarsSalary',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='SingleCarmodel',
        ),
    ]