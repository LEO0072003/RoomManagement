from .models import Events, Rooms, Bookings
from django.contrib import admin

# Register your models here.

admin.site.register(Events)
admin.site.register(Rooms)
admin.site.register(Bookings)
