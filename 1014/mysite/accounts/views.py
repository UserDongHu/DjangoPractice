from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from .forms import CreateUserForm
from django.urls import reverse_lazy
from blog.models import Post

login = LoginView.as_view(
    template_name = 'accounts/form.html',
    next_page = "main:index"
)

logout = LogoutView.as_view(
    next_page = "main:index"
)

signup = CreateView.as_view(
    form_class = CreateUserForm,
    template_name = 'accounts/form.html',
    success_url=reverse_lazy('accounts:login')
)

@login_required
def profile(request):
    post = Post.objects.filter(auth=request.user.username)
    return render(request, 'accounts/profile.html', {'post': post})