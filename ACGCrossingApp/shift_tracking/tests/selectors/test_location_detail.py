from django.test import TestCase
from ..factories import LocationFactory

from ...models.location import Location
from ...selectors.locations_get import get_location

class GetLocationDetailSelectorTests(TestCase):
    def test_selector_returns_location_happy_path(self):
        """
        This is a happy path test.
        If we create a user then ask for that user by their id,
        the selector should return the user.
        """
        location_from_creation = LocationFactory()
        location_id = location_from_creation.id
        location_from_selector = get_location(id=location_id)
        self.assertEqual(location_from_selector, location_from_creation)
    
    # Test some edge cases here