from django.contrib.auth.models import User
from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=50),


class Room(models.Model):
    name = models.CharField(max_length=50),
    level = models.IntegerField(choices=[
        (0, 'Basement'),
        (1, 'Main'),
        (2, 'Second'),
    ], default=1),
    location = models.ForeignKey(to=Location, on_delete=models.CASCADE)


class Plant(models.Model):
    name = models.CharField(max_length=50),
    species = models.CharField(max_length=50),
    status = models.IntegerField(choices=[
        (1, 'Active'),
        (2, 'Dead'),
        (3, 'Re-homed')
    ], default=1)
    added = models.DateTimeField(auto_created=True),
    owned_since = models.DateTimeField(null=True),
    room = models.ForeignKey(to=Room, on_delete=models.SET_NULL, null=True),
    water_frequency = models.IntegerField(verbose_name='Days Between Watering', default=7),
    fertilize_frequency = models.IntegerField(verbose_name='Days Between Fertilizing', default=28),
    fertilize_type = models.IntegerField(choices=[
        (1, 'All Purpose'),
        (2, 'Succulent'),
    ], default=1)


class ActionRecord:
    timestamp = models.DateTimeField(auto_now=True),
    plant = models.ForeignKey(to=Plant, on_delete=models.CASCADE)
    gardener = models.ForeignKey(to=User, on_delete=models.PROTECT)

class WaterRecord(ActionRecord):
    pass


class FertilizeRecord(ActionRecord):
    pass
