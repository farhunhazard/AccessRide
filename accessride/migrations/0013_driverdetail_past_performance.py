# Generated by Django 4.2.2 on 2023-07-08 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accessride', '0012_driverdetail_driver_vehicle_accessible'),
    ]

    operations = [
        migrations.AddField(
            model_name='driverdetail',
            name='Past_Performance',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
