from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView

from .models import Room, Message


@login_required
def rooms(request):
    """Roomlar ro'yxatini ko'rsatadi."""
    rooms = Room.objects.all()
    return render(request, 'room/rooms.html', {'rooms': rooms})


@login_required
def room(request, slug):
    """Berilgan slug bo'yicha xonani va xabarlarni ko'rsatadi."""
    room = get_object_or_404(Room, slug=slug)
    messages = Message.objects.filter(room=room).order_by('timestamp')
    return render(request, 'room/room.html', {'room': room, 'messages': messages})


class CreatePostView(CreateView):
    """Yangi xona yaratish uchun ko'rish."""
    model = Room
    template_name = 'room/new_channel.html'
    fields = ['name', 'slug']


class ChatDeleteView(DeleteView):
    """Xonani o'chirish uchun ko'rish."""
    model = Room
    template_name = 'room/room_delete.html'
    success_url = reverse_lazy('rooms')
