from django.shortcuts import render
from django.http import HttpResponse

db = {
    1: {
        'title': '제목 1', 
        'contents': 'Post 1 body', 
        'img': 'https://picsum.photos/200/300'
        },
    2: {
        'title': '제목 2', 
        'contents': 'Post 2 body', 
        'img': 'https://picsum.photos/200/300'
        },
    3: {
        'title': '제목 3', 
        'contents': 'Post 3 body', 
        'img': 'https://picsum.photos/200/300'
        },
    'i': {
        'hello'
    }
}

def blog(request):
    return render(request, 'blog/blog.html', {'db': db})

def post(request, pk):
    if db.get(pk):
        return render(request, 'blog/post.html', {'post': db.get(pk)})
    else:
        return HttpResponse('잘못된 접근입니다.')