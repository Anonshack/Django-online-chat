from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('room', args=[str(self.slug)])


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)
