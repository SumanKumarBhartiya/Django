from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from rest_framework import serializers



class UserLoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password =serializers.CharField()

    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]