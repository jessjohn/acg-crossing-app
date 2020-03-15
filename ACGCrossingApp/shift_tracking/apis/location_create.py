from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..services.location_create import create_location

class LocationCreateApi(APIView):
    class InputSerializer(serializers.Serializer):
        address = serializers.CharField()
        zone = serializers.CharField()
        latitude = serializers.FloatField()
        longitude = serializers.FloatField()
        description = serializers.CharField()
        location_number = serializers.IntegerField()
    

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        create_location(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)