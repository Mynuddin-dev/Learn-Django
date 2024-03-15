from django.contrib import admin

# Register your models here.

from .models import Room , Topic , Message

admin.site.register(Room) # Register the Room model to the admin site
admin.site.register(Topic) # Register the Topic model to the admin site
admin.site.register(Message) # Register the Message model to the admin site