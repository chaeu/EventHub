from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Event(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    guest_host = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name="participants", blank=True)
    capacity = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return self.name
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
    