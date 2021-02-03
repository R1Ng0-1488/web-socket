from django import forms

from .models import Room, Message


class RoomOrCreateForm(forms.ModelForm):
	name = forms.CharField(label='What chat room would you like to enter',
		widget=forms.TextInput(attrs={'id': 'room-name-input', 'type':'text', 'size': '100'})
		)
	class Meta:
		model = Room
		fields = '__all__'

	def save(self):
		room = Room.objects.get_or_create(name=self.cleaned_data['name'])
		return room[0]


# class CreateMessageForm(forms.ModelForm):
# 	class Meta:
# 		model = Message
# 		fields = '__all__'
# 		widgets = {'user': forms.HiddenInput}