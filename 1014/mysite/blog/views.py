from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
import os
from django.contrib.auth.decorators import login_required

def post(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post.html', {'post': post})

@login_required
def create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            post.auth = request.user.username
            post.save()
            return redirect('blog:post', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/create.html', {'form': form})

@login_required
def update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user.username == post.auth:
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save()
                return redirect('blog:post', pk=post.pk)
        else:
            form = PostForm(instance=post)
            return render(request, 'blog/create.html', {'form': form})
    else:
        return render(request, 'blog/post.html', {'post': post})

@login_required
def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user.username == post.auth:
        if request.method == "POST":
            if request.POST['confirm'] == '네':
                if post.main_image: # 사진 있으면
                    if os.path.exists(post.main_image.path): # 사진 파일 있으면
                        os.remove(post.main_image.path) # 삭제
                post.delete()
                return redirect('main:index')
            else:
                return render(request, 'blog/post.html', {'post': post})
        else:
            return render(request, 'blog/delete.html', {'post': post})
    else:
        return render(request, 'blog/post.html', {'post': post})