from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from ...apis.location_create import LocationCreateApi
from ...models import Location

class LocationCreateAPIViewTests(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()

        self.acceptable_address = "Villa Straylight"
        self.acceptable_zone = "Freeside"
        self.acceptable_latitude = 15
        self.acceptable_longitude = 120
        self.acceptable_description = "c'est wow"
        self.acceptable_location_number = 1

    def test_create_api_view_happy_path(self):
        request = self.factory.post(
            '/locations/create/',
            {
                'address': self.acceptable_address,
                'zone': self.acceptable_zone,
                'latitude': self.acceptable_latitude,
                'longitude': self.acceptable_longitude,
                'description': self.acceptable_description,
                'location_number': self.acceptable_location_number
            }
        )
        view = LocationCreateApi.as_view()
        response = view(request)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        loc_matches = Location \
            .objects \
            .filter(address__exact=self.acceptable_address) \
            .count()

        self.assertEquals(loc_matches, 1)
