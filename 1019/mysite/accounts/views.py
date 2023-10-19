from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

signup = CreateView.as_view(
    form_class = UserCreationForm,
    template_name = 'accounts/form.html',
    success_url = reverse_lazy('accounts:login')
)

login = LoginView.as_view(
    template_name = 'accounts/form.html',
)

logout = LogoutView.as_view(
    next_page = reverse_lazy('accounts:login'),
)

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'

profile = ProfileView.as_view()