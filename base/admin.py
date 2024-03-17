from django.contrib import admin

# Register your models here.

from .models import Type, Event, Message

admin.site.register(Type)
admin.site.register(Event)
admin.site.register(Message)
