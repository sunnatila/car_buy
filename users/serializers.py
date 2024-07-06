from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Cars


class CarSerializer(serializers.ModelSerializer):
    car_active = serializers.BooleanField(default=True)

    class Meta:
        model = Cars
        fields = ['id', 'car_brand', 'car_model', 'car_color', 'car_create_day', 'car_price', 'car_active']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
