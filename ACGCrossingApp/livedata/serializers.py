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
    user_id = serializers.IntegerField(write_only=True)
    shift_id = serializers.IntegerField(write_only=True)
    checked_in = serializers.CharField(max_length=2, min_length=2)
    date = serializers.DateField()
    shift_user = UserSerializer(required=False)
    shift = ShiftSerializer(required=False)

    def create(self, validated_data):
        uid = validated_data.get('user_id')
        sid = validated_data.get('shift_id')
        user = CustomUser.objects.get(pk=uid)
        shift = Shift.objects.get(pk=sid)
        return UserShift.objects.create(
            shift=shift,
            shift_user=user,
            checked_in=validated_data.get('checked_in'),
            date=validated_data.get('date')
        )

    def update(self, instance, validated_data):
        instance.shift = Shift.objects.get(pk=validated_data.get('shift_id'))
        instance.shift_user = CustomUser.objects.get(pk=validated_data.get('user_id'))
        instance.checked_in = validated_data.get('checked_in', instance.checked_in)
        instance.date = validated_data.get('date', instance.date)