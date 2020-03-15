import simplejson as json

from random import choice
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from ..factories import LocationFactory
from ...apis.location_detail import LocationDetailAPI
from ...models import Location

class LocationDetailAPIViewTests(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
    
    def test_detail_api_view_happy_path(self):
        loc_list = []
        for i in range(10):
            loc = LocationFactory()
            loc_list.append(loc)
        
        interested_location = choice(loc_list)
        request = self.factory.get(
            '/locations/{}/'.format(interested_location.id),
            format='json'
        )
        view = LocationDetailAPI.as_view()
        response = view(request, location_id=interested_location.id)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        
        expected = {
            'id': interested_location.id,
            'address': interested_location.address,
            'zone': interested_location.zone,
            'latitude': interested_location.latitude,
            'longitude': interested_location.longitude,
            'description': interested_location.description,
            'location_number': interested_location.location_number
        }

        self.assertJSONEqual(
            json.dumps(expected), 
            str(response.render().content, encoding='utf8')
        )