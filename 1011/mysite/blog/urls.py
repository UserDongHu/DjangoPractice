from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('write/', views.write, name='write'),
    path('<int:pk>/', views.post, name='post'),
]
