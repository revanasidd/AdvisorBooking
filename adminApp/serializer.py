
from rest_framework import serializers
from django.contrib.auth.models import User
from adminApp.models import UserModel


# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','password')
    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    email = serializers.CharField()
    username = serializers.CharField()
    class Meta:
        model = User
        fields = ['username','password','email']

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id','username','email','password')