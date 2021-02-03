from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Room(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Message(models.Model):
	text = models.TextField()
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	room = models.ForeignKey(Room, on_delete=models.CASCADE)

	def __str__(self):
		if self.user:
			return f"{self.user.username} - {self.room}"
		else:
			return f"anonymous - {self.room}"