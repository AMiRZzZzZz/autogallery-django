# Generated by Django 4.1.4 on 2022-12-25 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='singlecarmodel',
            name='CarsLuggage',
            field=models.IntegerField(choices=[(1, '2'), (2, '3'), (3, '4'), (4, '5')], default=2),
        ),
        migrations.AddField(
            model_name='singlecarmodel',
            name='Cars_Seats',
            field=models.IntegerField(choices=[(1, '2'), (2, '4'), (3, '5')], default=2),
        ),
    ]
