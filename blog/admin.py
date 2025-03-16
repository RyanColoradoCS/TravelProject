from django.contrib import admin

# Register your models here.

from .models import Post, GoogleMapsData, Locations, Location, Trip

admin.site.register(Post)
admin.site.register(GoogleMapsData)
admin.site.register(Locations)
admin.site.register(Location)
admin.site.register(Trip)