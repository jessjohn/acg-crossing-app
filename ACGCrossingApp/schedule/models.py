from django.db import models


class Location(models.Model):
    """
    Location model
    """
    address = models.CharField(max_length=256, blank=True, default='')
    zone = models.IntegerField
    lon = models.FloatField()
    lat = models.FloatField()

class Shift(models.Model):
    """
    Shifts Model
    """
<<<<<<< HEAD
    location = models.ForeignKey(
        Location,
        on_delete=models.PROTECT
    )
=======
   # location = models.ForeignKey()
>>>>>>> fbb9da8f524a880d900cc20e27b13c36f4229389
    start_time = models.TimeField()
    end_time = models.TimeField()