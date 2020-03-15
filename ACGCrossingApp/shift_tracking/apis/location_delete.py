from rest_framework import serializers
from rest_framework.views import APIView
from ..services.location_delete import delete_location
from rest_framework import status
from rest_framework.response import Response

class LocationDeleteApi(APIView):
    def delete(self, request, location_id):
        delete_location(location_id=location_id)
        return Response(status=status.HTTP_204_NO_CONTENT)