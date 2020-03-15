import simplejson as json

from random import choice
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from ..factories import LocationFactory
from ...apis.location_list import LocationListAPI
from ...models import Location

class LocationListAPIViewTests(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
    
    def test_list_api_view_happy_path(self):
        loc_list = []
        for i in range(10):
            loc = LocationFactory()
            loc_list.append(loc)
        
        request = self.factory.get(
            '/locations/',
            format='json'
        )
        view = LocationListAPI.as_view()
        response = view(request)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        expected = list(
            map(
                lambda x: {'id': x.id,'address': x.address,'zone': x.zone,'latitude': x.latitude,'longitude': x.longitude,'description': x.description,'location_number': x.location_number},
                loc_list
            )
        )

        self.assertJSONEqual(
            json.dumps(expected), 
            str(response.render().content, encoding='utf8')
        )