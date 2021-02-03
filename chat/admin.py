from django.contrib import admin

# Register your models here.
from .models import Room, Message


class MessageInline(admin.TabularInline):
	model = Message
		

@admin.register(Room)
class Room(admin.ModelAdmin):
	inlines = [MessageInline]