from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    # 글 목록
    path("", views.Index.as_view(), name='list'), #/post/
    # 글 상세 조회
    path("detail/<int:pk>/", views.DetailView.as_view(), name='list'), #/post/detail/pk/
    # 글 작성
    path("write/", views.Write.as_view(), name='write'), #/post/write/
    # 글 수정
    path("detail/<int:pk>/edit/", views.Update.as_view(), name='edit'), #/post/detail/pk/edit/
    # 글 삭제
    path("detail/<int:pk>/delete/", views.Delete.as_view(), name='delete'), #/post/detail/pk/delete/
    # 카테고리
    path('categories/', views.CategoryList.as_view(), name='category_list'),    
    # 검색 글 목록
    path('posts/', views.PostList.as_view(), name='post_list'),

]