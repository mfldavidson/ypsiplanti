from django.contrib import admin

from plants import models


@admin.register(models.Location)
class LocationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Plant)
class PlantAdmin(admin.ModelAdmin):
    pass
