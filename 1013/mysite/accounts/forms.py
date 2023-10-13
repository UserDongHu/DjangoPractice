from django import forms
from django.contrib.auth.forms import UserCreationForm
# 장고의 유저 관련 내장 모델
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm): # 장고에서 기본 제공하는 모델을 상속 받는다
    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2']