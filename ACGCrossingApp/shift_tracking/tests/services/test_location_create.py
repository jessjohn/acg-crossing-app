from django.test import TestCase
from ...services.location_create import create_location

class CreateLocationServiceTests(TestCase):
    acceptable_address = "Villa Straylight"
    acceptable_zone = "Freeside"
    acceptable_latitude = 15
    acceptable_longitude = 120
    acceptable_description = "c'est wow"
    acceptable_location_number = 1
    
    def test_create_location_from_service_happy_path(self):
        loc = create_location(
            address=self.acceptable_address,
            zone=self.acceptable_zone,
            latitude=self.acceptable_latitude,
            longitude=self.acceptable_longitude,
            description=self.acceptable_description,
            location_number=self.acceptable_location_number
        )
        self.assertEqual(str(loc), loc.address)