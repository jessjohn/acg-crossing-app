from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models.location import Location
from ..selectors.locations_get import get_location

class LocationDetailAPI(APIView):
    # For detail views, we just want to 
    # take an accurate representation of the
    # model and pass it along.
    
    # Only return a single location
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Location
            fields = (
                'id',
                'address',
                'zone',
                'latitude',
                'longitude',
                'description',
                'location_number'
            )

    def get(self, request, location_id):
        location = get_location(id=location_id)
        serializer = self.OutputSerializer(location)
        return Response(serializer.data)