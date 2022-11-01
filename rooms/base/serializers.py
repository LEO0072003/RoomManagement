from .models import Bookings, Rooms, Events
from rest_framework import serializers


class RoomSeraializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'

class EventSeraializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'

class BookSeraializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = '__all__'
