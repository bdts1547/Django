from django.db import models
from datetime import datetime


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self) -> str:
        return self.name
    

class Message(models.Model):
    text = models.CharField(max_length=1000000)
    username = models.CharField(max_length=20)
    time_created = models.DateTimeField(default=datetime.now)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)


