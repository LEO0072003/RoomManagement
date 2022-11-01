from rest_framework.response import Response
from rest_framework import (
    status,
    )
from .models import (Events, Rooms)
from rest_framework.decorators import api_view

from .serializers import (
                    BookSeraializer,
                    RoomSeraializer,
                    EventSeraializer,
)
from base import serializers

@api_view(['GET'])
def getEvents(request):
    events = Events.objects.filter(event_type='public')
    serializer = EventSeraializer(events, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def createEvents(request):
    serializer = EventSeraializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def createRooms(request):
    serializer = RoomSeraializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def createRooms(request):
    serializer = BookSeraializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
