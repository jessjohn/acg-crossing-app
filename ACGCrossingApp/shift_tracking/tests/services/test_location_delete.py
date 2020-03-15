from django.test import TestCase
from ...models import Location
from ..factories import LocationFactory

from ...services.location_delete import delete_location

class DeleteLocationServiceTests(TestCase):
    def test_delete_location_service_happy_path(self):
        created_location = LocationFactory()
        delete_location(location_id=created_location.id)
        self.assertEqual(Location.objects.count(), 0)

