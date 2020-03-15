from django.db.models import Model, CharField, FloatField, IntegerField, TextField
from django.core.validators import MaxValueValidator, MinValueValidator

class Location(Model):
    """
    In the data provided by OSC, we don't get concrete
    street adresses. They usually provide a brief string description,
    e.g. 'Street1 & Street2'
    
    An address should be required.
    An address should be unique.
    """
    address = CharField(
        max_length=255,
        unique=True
    )
    
    """
    We don't have specifications on what OSC calls a zone,
    there appears to be some technicality to this, but we will
    keep this as a string until presented with adequeate motivation
    to refactor this into its own model.
    Every data point has a zone at the moment, so we will require it.
    """
    zone = CharField(
        max_length=255
    )
    
    """
    Inetegers representing latitude and longitude in degrees.
    
    We require a latitude and logitude for visual representation
    of locations in the map UI.
    These should be provided and required at the time of creation.
    """
    latitude = FloatField(
        validators=[
            MaxValueValidator(90),
            MinValueValidator(-90)
        ],
        help_text="Latitude should be between -90 and 90 degrees."
    )

    longitude = FloatField(
        validators=[
            MaxValueValidator(180),
            MinValueValidator(-180)
        ],
        help_text="Longitude should be between -180 and 180 degrees."
    )
    
    """
    An optional longer text description of the location.
    """
    description = TextField(
        blank=True   
    )
    
    """
    Integer value found in the OSC dataset, while we have unique id's
    from the AutoField, this likely has a meaningful representation to
    the adminstrators of the program and we should track it.
    """
    location_number = IntegerField()

    """
    TODO: t.m.dubiel@gmail.com Feb 9 2020 - create a better string representation
    """
    def __str__(self):
        return self.address
    
    def __unicode__(self):
        return self.address