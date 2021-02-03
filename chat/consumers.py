from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

from django.contrib.auth.models import User
from .models import Room, Message

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.room = Room.objects.get(name=self.room_name)
        print('Connecttt', self.room_name, self.room_group_name, self.channel_layer.group_add)
        self.accept()

    def disconnect(self, close_code):
        print('disconnectttt', close_code, self.room_group_name,
            self.channel_name)
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        self.room = None

    def receive(self, text_data):
        print('receive', text_data)
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']
        print(username)
        if username == 'ANoNyMous':
        	Message.objects.create(text=message, room=self.room)
        else:
        	Message.objects.create(text=message, user=User.objects.get(username=username), room=self.room)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )

    def chat_message(self, event):
        print('chat_message', event)
        message = event['message']
        username = event['username']

        self.send(text_data=json.dumps({
            'event': "Send",
            'message': message,
            'username': username
        }))