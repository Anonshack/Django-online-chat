from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

from .models import Room, Message


@login_required
def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'room/rooms.html', {'rooms': rooms})


@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0::]
    return render(request, 'room/room.html', {'room': room, 'messages': messages})


class CreatePostView(CreateView):
    model = Room
    template_name = 'room/new_channel.html'
    fields = ['name', 'slug']


class ChatDeleteView(DeleteView):
    model = Room
    template_name = 'room/room_delete.html'
    success_url = reverse_lazy('rooms')