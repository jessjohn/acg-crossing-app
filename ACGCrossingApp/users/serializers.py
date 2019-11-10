# users/serializers.py
from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('id', 'email', 'username', )

class UserSerializerByName(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('username')