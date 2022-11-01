from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    # path('createRooms/', views.createRoom, name='createroom'),
    path('getevents/', views.getEvents),
    path('createevents/', views.createEvents),
        path('createroom/', views.createRooms),

]
