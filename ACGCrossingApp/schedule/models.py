from django.db import models
from math import cos, pi


# radius of earth approx
R = 6378137
# offset in metres
dg = 50

# add 50 m to the lat/lon values
def add_geo(lat, lon):
    d_lat = dg/R
    d_lon = dg/(R*cos(pi*lat/180))
    return (lat + d_lat * 180/pi, lon + d_lon * 180/pi)

# subtract 50m to the lat/lon values
def sub_geo(lat, lon):
    d_lat = dg/R
    d_lon = (R*cos(pi*lat/180))
    return (lat - d_lat * 180/pi, lon - d_lon * 180/pi)

class Location(models.Model):
    """
    Location model
    """
    address = models.CharField(max_length=256, blank=True, default='')
    zone = models.IntegerField(default=-1)
    lon = models.FloatField()
    lat = models.FloatField()
    
    @property
    def lat_plus(self):
        return add_geo(self.lat, self.lon)[0]

    @property
    def lon_plus(self):
        return add_geo(self.lat, self.lon)[1]

    @property
    def lat_minus(self):
        return sub_geo(self.lat, self.lon)[0]

    @property
    def lon_minus(self):
        return sub_geo(self.lat, self.lon)[0]

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