from django.test import TestCase
from django.db.utils import IntegrityError, DataError

from ...models.location import Location

class LocationTest(TestCase):
    # Declare some acceptable values
    acceptable_address = "Villa Straylight"
    acceptable_zone = "Freeside"
    acceptable_latitude = 15
    acceptable_longitude = 120
    acceptable_description = "c'est wow"
    acceptable_location_number = 1
    
    # Edge case
    char_field_exactly_255 = (
        "qAEyvcIUeztzskhfnTEUn"
        "7jhc0x68RywHXEAvPWZOv"
        "0ldutRNWAnb4iv3LTjK6W"
        "XFv0T0j5tQ9e3iuEOMwaV"
        "VanXsJP0r4Z0L7maxKvIS"
        "CMNm9neZuv8XSpYzpxZf1"
        "Ev8wMug43uebU5NGeKmtN"
        "zpgAjB6Zf8pebf5l5p5iF"
        "SZuDXiTQaGv6c30liIjlb"
        "3uNoCHP66iDlll2X6m566"
        "K4WhEMe3bZiTDKBurdqfm"
        "Ce76KbEgZierHembCDR3D"
        "fea"
    )

    # Delcare some unacceptable values
    null_value = None
    char_field_over_255 = char_field_exactly_255 + "q"
    lat_too_low = -91
    lat_too_high = 91
    lon_too_low = -181
    long_too_high = 181

    def test_happy_path(self):
        loc = Location.objects.create(
            address=self.acceptable_address,
            zone=self.acceptable_zone,
            latitude=self.acceptable_latitude,
            longitude=self.acceptable_longitude,
            description=self.acceptable_description,
            location_number=self.acceptable_location_number
        )
        self.assertEqual(str(loc), loc.address)

    """
    Validating non-nullable fields:
    
    
    - address field: Ensure that trying to create a location with no
    address throws an integrity error when all other fields
    are acceptable values
    """
    def test_address_required(self):
        with self.assertRaises(IntegrityError):
            Location.objects.create(
                address=self.null_value,
                zone=self.acceptable_zone,
                latitude=self.acceptable_latitude,
                longitude=self.acceptable_longitude,
                description=self.acceptable_description,
                location_number=self.acceptable_location_number
            )
    """
    - address field: should be less than 255 characters
    """
    def test_address_too_long(self):
        with self.assertRaises(DataError):
            Location.objects.create(
                address=self.char_field_over_255,
                zone=self.acceptable_zone,
                latitude=self.acceptable_latitude,
                longitude=self.acceptable_longitude,
                description=self.acceptable_description,
                location_number=self.acceptable_location_number
            )
    
    """
    - zone field: Ensure that trying to create a location with no
    zone throws an integrity error.
    """
    def test_zone_required(self):
        with self.assertRaises(IntegrityError):
            Location.objects.create(
                address=self.acceptable_address,
                zone=self.null_value,
                latitude=self.acceptable_latitude,
                longitude=self.acceptable_longitude,
                description=self.acceptable_description,
                location_number=self.acceptable_location_number
            )
