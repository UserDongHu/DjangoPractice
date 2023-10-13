from django.shortcuts import render, get_object_or_404, redirect # 추가
from .models import Post
from django.db.models import Q # 쿼리 객체 Q import
from .forms import PostForm # forms.py 에서 PostForm클래스 import

def index(request):
    if request.GET.get('q'): # GET요청에서 q가 있으면 : 검색 버튼을 눌렀을때
        q = request.GET.get('q')
        db = Post.objects.filter(Q(title__icontains=q) | Q(contents__icontains=q)).distinct() # Q 객체를 이용해서 &(and)와 |(or) 연산을 할 수 있다. distinct() : 중복 제거
    else:
        db = Post.objects.all()
    context = {
        'db': db,
    }
    return render(request, 'blog/index.html', context)

def post(request, pk):
    db = Post.objects.get(pk=pk)
    context = {
        'db': db,
    }
    return render(request, 'blog/post.html', context)

# def create(request): # 게시물 생성
#     if request.method == "POST": # request가 POST면 : 게시 버튼을 누르면
#         form = PostForm(request.POST, request.FILES) # PostForm에 Post요청값과 파일들을 넣어서 form 생성.
#         if form.is_valid(): # form 유효성 검사 : DB와 형식이 일치하면
#             post = Post( # Post객체 post 생성
#                 title = form.cleaned_data['title'], # 아까 만든 form의 cleaned_data를 이용해서 dict형태로 접근
#                 contents = form.cleaned_data['contents'],
#                 main_image = form.cleaned_data['main_image'],
#             )
#             post.save() # DB에 저장
#             return redirect('blog:post', pk=post.pk) # 생성 후 게시물의 상세보기로 이동.
#     else:
#         form = PostForm() # POST 요청이 아니면 PostForm형식에 맞게 form 생성
#     return render(request, 'blog/create.html', {'form': form})

# def update(request, pk): # 게시물 수정 (업데이트)
#     post = get_object_or_404(Post, pk=pk) # get_object_or_404 : Post.obejcts.get(pk=pk)가 있으면 post로 지정, 없으면 404를 반환하는 함수
#     if request.method == "POST": # request가 POST면 : 수정하기를 누르면
#         form = PostForm(request.POST, request.FILES) # request로 form 생성
#         if form.is_valid(): # form 유효성 검사 : DB와 형식이 일치하는지
#             post.title = form.cleaned_data['title'] # 요소 하나씩 수정
#             post.contents = form.cleaned_data['contents']
#             if form.cleaned_data['main_image']:
#                 post.main_image = form.cleaned_data['main_image']
#             post.save() # DB에 저장
#         return redirect('blog:post', pk=post.pk) # 수정 후 게시물의 상세보기로 이동
#     else:
#         initial_data = { # 수정하기 전 게시물 데이터 값 받아오기
#         'title': post.title,
#         'contents': post.contents,
#         'main_image': post.main_image,
#         }
#         form = PostForm(initial=initial_data) # 수정 하기 전 게시물 데이터를 넣은 PostForm으로 생성
#     return render(request, 'blog/create.html', {'form': form})

def create(request): # 게시물 생성
    if request.method == "POST": # request가 POST면 : 게시 버튼을 누르면
        form = PostForm(request.POST, request.FILES) # PostForm에 Post요청값과 파일들을 넣어서 form 생성.
        if form.is_valid(): # form 유효성 검사 : DB와 형식이 일치하면
            post = form.save() # ModelForm일때는 이렇게 DB에 저장가능
            return redirect('blog:post', pk=post.pk) # 생성 후 게시물의 상세보기로 이동.
    else:
        form = PostForm() # POST 요청이 아니면 PostForm형식에 맞게 form 생성
    return render(request, 'blog/create.html', {'form': form})

def update(request, pk): # 게시물 수정 (업데이트)
    post = get_object_or_404(Post, pk=pk) # get_object_or_404 : Post.obejcts.get(pk=pk)가 있으면 post고 없으면 404를 반환하는 함수
    if request.method == "POST": # request가 POST면 : 수정하기를 누르면
        form = PostForm(request.POST, request.FILES, instance=post) # instance=post : ModelForm은 instance 매개변수를 통해 수정할 모델 객체 지정
        if form.is_valid(): # form 유효성 검사 : DB와 형식이 일치하는지
            form.save() # DB에 저장
            return redirect('blog:post', pk=post.pk) # 수정 후 게시물의 상세보기로 이동
    else:
        form = PostForm(instance=post) # ModelForm은 instance매개변수를 이용해서 form의 값을 미리 받아온다.
    return render(request, 'blog/create.html', {'form': form})

def delete(request, pk): # 게시물 삭제
    post = get_object_or_404(Post, pk=pk) # get_object_or_404 : Post.obejcts.get(pk=pk)가 있으면 post로 지정, 없으면 404를 반환하는 함수
    if request.method == "POST": # POST요청이면 : 삭제 버튼을 눌렀으면
        post.delete() # 지정한 post를 DB에서 삭제
        return redirect('blog:index') # 삭제한 후 메인으로 이동
    return render(request, 'blog/delete.html', {'post': post}) # post 요청이 아닐때는 delete.html render해주기