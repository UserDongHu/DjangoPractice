# chat/urls.py

from django.urls import path
from .views import MessageCreateView, RoomCreateView, RoomDetailView
from .views import ChatView


urlpatterns = [
    path('', ChatView.as_view(), name='chat'),
    path('message/', MessageCreateView.as_view(), name='message-create'),
    path('room/', RoomCreateView.as_view(), name='room-create'),
    path('room/<int:room_id>/', RoomDetailView.as_view(), name='room-detail'),
]
