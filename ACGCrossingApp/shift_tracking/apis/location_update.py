from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from ..services.location_update import update_location

class LocationUpdateAPI(APIView):
    class InputSerializer(serializers.Serializer):
        address = serializers.CharField()
        zone = serializers.CharField()
        latitude = serializers.FloatField()
        longitude = serializers.FloatField()
        description = serializers.CharField()
        location_number = serializers.IntegerField()

    def post(self, request, location_id):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        update_location(location_id=location_id, **serializer.validated_data)

        return Response(status=status.HTTP_200_OK)
