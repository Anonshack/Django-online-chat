from django.urls import path
from . import views
from .views import CreatePostView, ChatDeleteView

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('<slug:slug>/', views.room, name='room'),
    path('new/channel/', CreatePostView.as_view(), name='new-channel'),
    path('rooms/channel/<int:pk>/delete/', ChatDeleteView.as_view(), name='channel-delete'),
]