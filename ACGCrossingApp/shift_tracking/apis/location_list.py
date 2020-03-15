from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from ..models.location import Location
from ..selectors.locations_get import get_locations

class LocationListAPI(APIView):
    # Return a list of detail-locations
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
    
    def get(self, request):
        locations = get_locations()
        serializer = self.OutputSerializer(locations, many=True)
        return Response(serializer.data)