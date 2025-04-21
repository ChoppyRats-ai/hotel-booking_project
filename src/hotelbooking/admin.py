from django.contrib import admin

from .models import Booking, Room

# Register your models here.

admin.site.register(Room)
admin.site.register(Booking)