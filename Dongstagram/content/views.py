from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Feed
from uuid import uuid4
import os
from user.models import User
from Dongstagram.settings import MEDIA_ROOT

class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all().order_by('-id')
        print('로그인한 사용자 : ', request.session['email'])
        email = request.session['email']
        user = User.objects.filter(email=email).first()
        if email is None:
            return render(request, 'user/login.html')
        if user is None:
            return render(request, 'user/login.html')
        return render(request, 'Dongstagram/main.html', context=dict(feeds=feed_list, user=user))
class UploadFeed(APIView):
    def post(self, request):

        file = request.FILES['file']

        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)

        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        
        
        image = uuid_name
        content = request.data.get('content')
        user_id = request.data.get('user_id')
        profile_image = request.data.get('profile_image')

        Feed.objects.create(image=image, content=content, user_id=user_id, profile_image=profile_image,like_count = 0)

        return Response(status=200)