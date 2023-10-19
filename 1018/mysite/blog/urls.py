from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.postlist, name='postlist'),
    path('<int:pk>/', views.postdetail, name='postdetail'),
]