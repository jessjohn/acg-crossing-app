from rest_framework import serializers
from .models import Location, Shift


class LocationSerializer(serializers.ModelSerializer):
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

class ShiftSerializer(serializers.Serializer):
    """
    Shift Serializer
    """
    start_time = serializers.TimeField()
    end_time = serializers.TimeField()
    location = LocationSerializer()

    def create(self, validated_data):
        """
        Create a new serialized shift given validated data
        """
        return Shift.objects.create(**validated_data)

class ShiftWriteSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    location_id = serializers.IntegerField()
    start_time = serializers.TimeField()
    end_time = serializers.TimeField()
    location = LocationSerializer(required=False)


    def create(self, validated_data):
        # TODO: start time should be after end time.
        """
        Create a new serialized shift given validated data
        """
        pk = validated_data.get('location_id')
        location = Location.objects.get(pk=pk)
        return Shift.objects.create(
            location=location,
            start_time=validated_data.get('start_time'),
            end_time=validated_data.get('end_time')
        )

    def update(self, instance, validated_data):
        instance.location = Location.objects.get(pk=validated_data.get('location', instance.location))
        instance.start_time = validated_data.get('start_time', instance.start_time)
        instance.end_time = validated_data.get('start_time', instance.end_time)
        instance.save()
        return instance
