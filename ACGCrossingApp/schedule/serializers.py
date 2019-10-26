from rest_framework import serializers
from .models import Location


class LocationSerializer(serializers.Serializer):
    """
    Locations serializer
    """
    class Meta:
        model = Location
        fields = ['id', 'address', 'zone', 'lon', 'lat']

    def create(self, validated_data):
        """
        Create and return a new `Locations` instance, given the validated data.
        """
        return Location.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Locations` instance, given the validated data.
        """
        instance.address = validated_data.get('address', instance.address)
        instance.zone = validated_data.get('zone', instance.zone)
        instance.lon = validated_data.get('lon', instance.lon)
        instance.lat = validated_data.get('lat', instance.lat)
        instance.save()
        return instance
