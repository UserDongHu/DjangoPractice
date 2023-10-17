from django.shortcuts import render
from .models import Post, Comment, Tag
from .forms import CommentForm
from django.db.models import Q

def postlist(request):
    if request.GET.get('q'): # get요청의 q가 있으면
        q = request.GET.get('q')
        posts = Post.objects.filter(Q(title__icontains=q)|Q(content__icontains=q)|Q(comments__message__icontains=q)).distinct() # comments__message :model에서 related_name으로 설정한 comments인 Comment모델의 message필드
    else:
        posts = Post.objects.all()
    return render(request, 'blog/postlist.html', {'posts':posts})

def postdetail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm() # 댓글폼
    if request.method == 'POST': # Post 요청이 들어오면
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) # DB에는 저장하지않는 임시 form으로 저장
            comment.author = request.user # author에 request.user 할당
            comment.post = post # 해당 댓글이 속하는 post 설정
            comment.save() # DB에 저장
    return render(request, 'blog/postdetail.html', {'post':post, 'form':form})

def posttag(request, tag):
    posts = Post.objects.filter(tags__name__iexact=tag) # tags모델의 name필드가 tag와 완벽하게 일치하는것들
    return render(request, 'blog/postlist.html', {'posts':posts})