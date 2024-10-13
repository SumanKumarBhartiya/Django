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

class UserRegisterSerializer(serializers.Serializer):

    username = serializers.CharField()
    name = serializers.CharField()
    password =serializers.CharField()
    confirm_password =serializers.CharField()

    class Meta:
        model = User
        fields = [
            'username',
            'name',
            'password',
            'confirm_passwword',
        ]
    
    def validate(self, attrs):
        username = attrs.get('username')
        try:
            user = User.objects.get(username = username)
            if user:
                raise serializers.ValidationError({'username': "User exists with the given username."})
        except User.DoesNotExist:
            pass
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError({"password" : "Password and confirm password do not match."})
        return super().validate(attrs)

    def create(self, validated_data):
        username = validated_data.get('username')
        name = validated_data.get('name')
        password = validated_data.get('password')

        user = User.objects.create(username = username, first_name = name )
        user.set_password(password)
        user.save()

        return True