from rest_framework import serializers,fields
from django.contrib.auth.models import User
from .models import AdvisorModel
class AdvisorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvisorModel
        fields = ('id','advname','image',)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class BookingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvisorModel
        fields = ('id','advname','image','booking_id','booking_date')
