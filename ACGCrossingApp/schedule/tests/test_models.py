from django.test import TestCase
from ..models import *
import datetime

class LocationTest(TestCase):
    """ Test module for Location model """
    def setUp(self):
        Location.objects.create(
            address="3 Fake Lane, Ottawa ON",
            zone=1,
            lon=75.7009,
            lat=45.4236
        )
        
        Location.objects.create(
            address="Bagend, Bagshot Row",
            zone=2,
            lon=0,
            lat=0
        )

    def test_locations(self):
        location_fake_lane = Location.objects.get(
            address="3 Fake Lane, Ottawa ON"
        )

        location_bagend = Location.objects.get(
            address="Bagend, Bagshot Row"
        )

        print()


class ShiftTest(TestCase):
    """ Test module for Shift model """
    def setUp(self):
        # Make a location so the shift can be attached to a place
        loc = Location.objects.create(
            address="3 Fake Lane, Ottawa ON",
            zone=1,
            lon=75.7009,
            lat=45.4236
        )

        # Make a shift template for the location
        Shift.objects.create(
            location=loc.id,
            start_time=datetime.time(17,0,0),
            end_time=datetime.time(18,0,0)
        )