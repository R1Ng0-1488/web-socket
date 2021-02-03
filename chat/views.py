import json

from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe

from .forms import RoomOrCreateForm
from .models import Room

# Create your views here.

def index(request):
	form = RoomOrCreateForm()
	if request.method == 'POST':
		form = RoomOrCreateForm(request.POST)
		if form.is_valid():
			room = form.save()
			return redirect('room', room.name)
	return render(request, 'chat/index.html', {'form': form})

def room(request, room_name):
	# room = Room.objects.get(name=room_name)
	# messages =  json.dumps({ message.user.username : message.text for message in room.message_set.all()})
	
	return render(request, 'chat/room.html', {
		'room_name_json': mark_safe(json.dumps(room_name)),
		'room_name': room_name,
		'messages': Room.objects.get(name=room_name).message_set.all(),
		'user_name': request.user.username if request.user.is_authenticated else 'ANoNyMous'
		# 'messages': messages
	})