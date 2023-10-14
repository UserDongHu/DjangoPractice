from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('post/<int:pk>/', views.post, name='post'),
    path('create/', views.create, name='create'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('update/<int:pk>/', views.update, name='update'),
]