from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from ..factories import LocationFactory
from ...apis.location_delete import LocationDeleteApi
from ...models import Location

class LocationDeleteAPIViewTests(TestCase):
    def setUp(self):
        self.request_factory = APIRequestFactory()

    def test_location_delete_api_view_happy_path(self):
        created_location = LocationFactory()
        request = self.request_factory.delete(
            '/locations/{}/'.format(created_location.id)
        )

        view = LocationDeleteApi.as_view()
        response = view(request, location_id=created_location.id)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        loc_matches = Location \
            .objects \
            .filter(id__exact=created_location.id) \
            .count()
        
        self.assertEquals(loc_matches, 0)
