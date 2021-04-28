from django.db import models

# Create your models here.

class DataSet(models.Model):
    GLOBAL = 'GB'
    NORTHERN_HEMISPHERE = 'NH'
    SOUTHERN_HEMISPHERE = 'SH'
    LOCATION_CHOICES = [
        (GLOBAL, 'GLOBAL'),
        (NORTHERN_HEMISPHERE, 'NORTHER_HEMISPHERE'),
        (SOUTHERN_HEMISPHERE, 'SOUTHERN_HEMISPHERE'),
    ]
    location = models.CharField(max_length=2, choices=LOCATION_CHOICES, default=GLOBAL)
    LAND = 'LD'
    WATER = 'WT'
    LAND_AND_WATER = 'LW'
    SURFACE_TYPE_CHOICES = [
        (LAND, 'LAND'),
        (WATER, 'WATER'),
        (LAND_AND_WATER, 'LAND_AND_WATER'),

    ]
    surface_type = models.CharField(max_length=2, choices=SURFACE_TYPE_CHOICES, default=LAND_AND_WATER)

class Measurement(models.Model):
    data_set = models.ForeignKey(DataSet, on_delete=models.CASCADE)
    date = models.DateField
    anomaly = models.FloatField
