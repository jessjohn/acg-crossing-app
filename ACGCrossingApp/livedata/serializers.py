from rest_framework import serializers
from .models import UserShift
from schedule.serializers import LocationSerializer, ShiftSerializer, ShiftWriteSerializer
from users.serializers import UserSerializer
from schedule.models import Location, Shift
from users.models import CustomUser

class UserShiftReadSerializer(serializers.Serializer):
    shift = ShiftSerializer()
    shift_user = UserSerializer()
    checked_in = serializers.CharField(max_length=2, min_length=2)
    date = serializers.DateField()

    def create(self, validated_data):
        """
        Create a new serialized shift given validated data
        """
        return Shift.objects.create(**validated_data)

class UserShiftWriteSerializer(serializers.Serializer):
    pass