from django.shortcuts import render
from django.http import HttpResponse

db = [
    {
        'id': 1,
        'title': '나의 죽음을 알리지 마라',
        'contents': '첫번째 게시물 내용',
        'created_at': '2023-10-10 00:00:00',
        'updated_at': '2023-10-11 00:00:00',
        'author': '이순신',
        'category': '일상',
        'tags': '체력단련, 무예단련',
        'thumbnail': 'https://picsum.photos/200/300',
    },
    {
        'id': 2,
        'title': '왕이 되고 싶은 나',
        'contents': '두번째 게시물 내용',
        'created_at': '2023-10-12 00:00:00',
        'updated_at': '2023-10-13 00:00:00',
        'author': '김유신',
        'category': '테크',
        'tags': '맥북, 아이폰, 파이썬',
        'thumbnail': 'https://picsum.photos/200/300',
    },
    {
        'id': 3,
        'title': '한글은 최고야',
        'contents': '세번째 게시물 내용',
        'created_at': '2023-10-14 00:00:00',
        'updated_at': '2023-10-15 00:00:00',
        'author': '세종대왕',
        'category': '취미',
        'tags': '그림, 서예',
        'thumbnail': 'https://picsum.photos/200/300',
    },
]

def index(request):
    return render(request, 'blog/index.html', {'db': db})

def post(request, pk):
    if len(db) >= pk:
        return render(request, 'blog/post.html', {'db': db[pk-1]})
    else:
        return HttpResponse('잘못된 접근입니다.')