from django.db import models

class detail(models.Model):
    passengers_name=models.CharField(max_length=100)
    passenger_image=models.ImageField(upload_to='photo')
    defect=models.CharField(max_length=100)
    address=models.TextField()
    phone_no=models.BigIntegerField()
    equipments=models.TextField()
    OPTION_ONE = 'Two Wheeler'
    OPTION_TWO = 'Four Wheeler'
    CHOICES = (
        (OPTION_ONE, 'Two Wheeler'),
        (OPTION_TWO, 'Four Wheeler'),
    )
    mode_of_ride = models.CharField(max_length=50, choices=CHOICES)
    passenger_feedback=models.CharField(max_length=100,blank=True)
    Gender=models.CharField(max_length=100)

class driverdetail(models.Model):
    driver_name=models.CharField(max_length=100)
    driver_image=models.ImageField(upload_to='photo')
    driver_address=models.TextField()
    driver_phoneno=models.BigIntegerField()
    driver_licenseno=models.CharField()
    driver_licenseimage=models.ImageField(upload_to='Verification')
    driver_demo=models.BooleanField()
    driver_reason=models.TextField()
    driver_experience_in_years=models.IntegerField()
    driver_training=models.BooleanField()
    driver_vehicle_accessible=models.BooleanField()
    Past_Performance=models.IntegerField()
    driver_attitude=models.CharField(max_length=50)
    driver_physical_ability=models.CharField(max_length=50)
    Gender=models.CharField(max_length=100)

