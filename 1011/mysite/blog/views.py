from django.shortcuts import render
from .models import Post
from django.db.models import Q

def index(request):
    if request.GET.get('q'):
        q = request.GET.get('q')
        db = Post.objects.filter(Q(title__icontains=q) | Q(contents__icontains=q)).distinct()
    else:
        db = Post.objects.all()
    context = {'db': db}
    return render(request, 'blog/index.html', context)

def write(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        contents = request.POST.get('contents')
        image = request.FILES.get('image')
        if title and contents and image:
            newpost = Post.objects.create(title=f'{title}', contents=f'{contents}', main_image=image)
            newpost.save()
        elif title and contents:
            newpost = Post.objects.create(title=f'{title}', contents=f'{contents}')
            newpost.save()
        return index(request)
    else:
        return render(request, 'blog/write.html')

def post(request, pk):
    db = Post.objects.get(pk=pk)
    context = {'db': db}
    return render(request, 'blog/post.html', context)