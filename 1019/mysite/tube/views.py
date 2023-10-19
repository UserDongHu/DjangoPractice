from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView
from .models import Post, Comment, Tag
from .forms import PostForm, CommentForm, TagForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class PostListView(ListView):
    model = Post
    
    def get_queryset(self): # DB에서 보여줄 쿼리셋을 가져오는 함수
        qs = super().get_queryset() # 전체 가져오기
        q = self.request.GET.get('q', '') # get요청일때 q값
        if q: # q값이 있으면
            qs = qs.filter(title__icontains=q) # q를 제목에 포함중인 쿼리셋만 가져오기
        return qs # 리턴
    
post_list = PostListView.as_view()
    
class PostTagListView(ListView): # 태그를 가진 게시물 리스트 보여주기
    model = Post
    
    def get_queryset(self):
        qs = super().get_queryset()
        tag = self.kwargs['tag']
        qs = qs.filter(tags__name__iexact=tag)
        q = self.request.GET.get('q', '')
        if q:
            qs = qs.filter(title__icontains=q)
        return qs
    
post_tag_list = PostTagListView.as_view()

class PostDetailView(DetailView):
    model = Post
    
    def get_context_data(self, **kwargs): # 원하는 쿼리셋이나 object를 추가해서 템플릿으로 전달
        context = super().get_context_data(**kwargs) # 원래 전달할 context데이터
        context['comment_form'] = CommentForm() # context데이터에 comment_form을 추가해서 같이 전달
        return context
    
    def get_object(self, queryset=None): # PostDetailView에서 사용할 object를 변경해서 반환.
        pk = self.kwargs['pk']
        post = Post.objects.get(pk=pk)
        post.view_count += 1
        post.save()
        return super().get_object(queryset)
    
post_detail = PostDetailView.as_view()

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'tube/form.html'
    
    def form_valid(self, form): # 폼이 유효한지 확인
        video = form.save(commit=False) # DB에 올리지 않고 임시 저장
        video.author = self.request.user # video의 author을 현재 user로 설정
        return super().form_valid(form) # 폼이 유효한지 확인하고 저장
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # 원래 전달할 context데이터
        context['tag_form'] = TagForm() # context데이터에 tag_form 추가해서 같이 전달
        return context
    
    def get_success_url(self): # 성공시 갈 url
        return reverse_lazy('tube:post_detail', kwargs={'pk': self.object.pk}) # kwargs로 방금 만든 게시물 pk를 전달
    
post_new = PostCreateView.as_view()

class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'tube/form.html'
    
    def get_success_url(self): # 성공시 갈 url
        return reverse_lazy('tube:post_detail', kwargs={'pk': self.object.pk}) # kwargs로 방금 만든 게시물 pk를 전달
    
    def test_func(self): # UserPassesTestMixin안의 메서드로 True, False로 접근 제한
        return self.get_object().author == self.request.user
    
post_edit = PostUpdateView.as_view()

class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    
    def get_success_url(self): # 성공시 갈 url
        return reverse_lazy('tube:post_list')
    
    def test_func(self): # UserPassesTestMixin안의 메서드로 True, False로 접근 제한
        return self.get_object().author == self.request.user
    
post_delete = PostDeleteView.as_view()

class CommentCreateView(LoginRequiredMixin, CreateView): # 댓글 달기
    model = Comment
    form_class = CommentForm
    
    def form_valid(self, form):
        pk = self.kwargs['pk']
        post = Post.objects.get(pk=pk)
        comment = form.save(commit=False)
        comment.author = self.request.user
        comment.post = post
        comment.save()
        return redirect('tube:post_detail', pk=pk)
    
comment_new = CommentCreateView.as_view()

class TagCreateView(CreateView): # 태그 생성하기
    model = Tag
    form_class = TagForm
    
    def form_valid(self, form):
        form.save()
        return redirect('tube:post_new')
    
tag_new = TagCreateView.as_view()