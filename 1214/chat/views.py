# chat/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Room  # 추가
# chat/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

class ChatView(TemplateView):
    template_name = 'chat/index.html'

class MessageCreateView(APIView):
    def post(self, request, *args, **kwargs):
        channel_layer = get_channel_layer()
        message_type = request.data.get('type', '')
        message = request.data.get('message', '')

        if message_type == 'chat.message':
            room_id = request.data.get('room_id', '')
            room_group_name = f'chat_{room_id}'
            async_to_sync(channel_layer.group_send)(
                room_group_name,
                {
                    'type': 'chat.message',
                    'message': message
                }
            )

            return Response({'detail': 'Message sent successfully.'}, status=status.HTTP_200_OK)

        return Response({'detail': 'Invalid message type.'}, status=status.HTTP_400_BAD_REQUEST)


class RoomCreateView(APIView):
    def post(self, request, *args, **kwargs):
        room_name = request.data.get('name', '')
        room = Room.objects.create(name=room_name)
        return Response({
            'id': room.id,
            'name': room.name,
            'chat_url': f'/ws/chat/{room.id}/chat/'
        }, status=status.HTTP_201_CREATED)


class RoomDetailView(APIView):
    def post(self, request, *args, **kwargs):
        room_id = kwargs.get('room_id')
        room = Room.objects.get(id=room_id)
        return Response({
            'id': room.id,
            'name': room.name,
            'chat_url': f'/ws/chat/{room.id}/chat/'
        })
