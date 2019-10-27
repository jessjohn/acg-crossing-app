from django.db import models


class Location(models.Model):
    """
    Location model
    """
    address = models.CharField(max_length=256, blank=True, default='')
    zone = models.IntegerField(default=-1)
    lon = models.FloatField()
    lat = models.FloatField()

class Shift(models.Model):
    """
    Shifts Model
    """
    location = models.ForeignKey(
        Location,
        on_delete=models.PROTECT
    )
    start_time = models.TimeField()
    end_time = models.TimeField()