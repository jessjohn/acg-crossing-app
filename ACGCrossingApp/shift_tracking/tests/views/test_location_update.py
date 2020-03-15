import simplejson as json

from django.forms.models import model_to_dict
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from ..factories import LocationFactory
from ...apis.location_update import LocationUpdateAPI
from ...models import Location

class LocationUpdatePIViewTests(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

        self.acceptable_address = "Villa Straylight"
        self.acceptable_zone = "Freeside"
        self.acceptable_latitude = 15
        self.acceptable_longitude = 120
        self.acceptable_description = "c'est wow"
        self.acceptable_location_number = 1

    def test_update_api_view_happy_path(self):
        original_location = LocationFactory()
        update_dict = {
            'address': self.acceptable_address,
            'zone': self.acceptable_zone,
            'latitude': self.acceptable_latitude,
            'longitude': self.acceptable_longitude,
            'description': self.acceptable_description,
            'location_number': self.acceptable_location_number
        }
        
        request = self.factory.post(
            '/locations/{}/update/'.format(original_location.id),
            update_dict,
            format='json'
        )

        view = LocationUpdateAPI.as_view()
        response = view(request, location_id=original_location.id)

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        updated_loc = Location.objects.get(pk=original_location.id)
        updated_loc_dict = model_to_dict(updated_loc)

        # add the id to the update dict to make sure it matches what we see in the db
        update_dict['id'] = original_location.id

        self.assertDictEqual(updated_loc_dict, update_dict)