from django.test import TestCase
from ..factories import LocationFactory

from ...models.location import Location
from ...selectors.locations_get import get_locations

class GetLocationListSelectorTests(TestCase):
    def test_selector_returns_location_list_happy_path(self):
        """
        This is a happy path test.
        If we create a bunch of users then ask for all users,
        the selector should return the user list.
        """
        loc_list = []
        for i in range(10):
            loc = LocationFactory()
            loc_list.append(loc)

        locations_from_selector = get_locations()
        # Make sure the sequence we generated matches 
        # the sequence we got back from the database
        self.assertSequenceEqual(locations_from_selector, loc_list)

    # Test some edge cases here