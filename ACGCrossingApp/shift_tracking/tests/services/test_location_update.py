from django.test import TestCase
from ..factories import LocationFactory
from ...models.location import Location

from ...services.location_update import update_location

class UpdateLocationServiceTests(TestCase):
    acceptable_address = "Villa Straylight"
    acceptable_zone = "Freeside"
    acceptable_latitude = 15
    acceptable_longitude = 120
    acceptable_description = "c'est wow"
    acceptable_location_number = 1

    def test_update_location_service_happy_path(self):
        factory_location = LocationFactory()
        updated_location = update_location(
            factory_location.id,
            address=self.acceptable_address,
            zone=self.acceptable_zone,
            latitude=self.acceptable_latitude,
            longitude=self.acceptable_longitude,
            description=self.acceptable_description,
            location_number=self.acceptable_location_number
        )
        location_from_db_after_update = Location.objects.get(id=factory_location.id)

        # address
        self.assertEqual(updated_location.address, self.acceptable_address)
        self.assertEqual(location_from_db_after_update.address, self.acceptable_address)

        # zone
        self.assertEqual(updated_location.zone, self.acceptable_zone)
        self.assertEqual(location_from_db_after_update.zone, self.acceptable_zone)

        # latitude
        self.assertEqual(updated_location.latitude, self.acceptable_latitude)
        self.assertEqual(location_from_db_after_update.latitude, self.acceptable_latitude)

        # longitude
        self.assertEqual(updated_location.longitude, self.acceptable_longitude)
        self.assertEqual(location_from_db_after_update.longitude, self.acceptable_longitude)

        # description
        self.assertEqual(updated_location.description, self.acceptable_description)
        self.assertEqual(location_from_db_after_update.description, self.acceptable_description)

        # location_number
        self.assertEqual(updated_location.location_number, self.acceptable_location_number)
        self.assertEqual(location_from_db_after_update.location_number, self.acceptable_location_number)