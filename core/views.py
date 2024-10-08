from django.contrib.auth import login
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import SignUpForm, PasswordChangeingForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


def frontpage(request):
    return render(request, 'core/frontpage.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('frontpage')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})


class UserListView(UserPassesTestMixin, ListView):
    model = User
    template_name = 'user/user_list.html'
    context_object_name = 'users'

    def test_func(self):
        return self.request.user.is_superuser


class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeingForm
    success_url = reverse_lazy('password-success')


def password_success(request):
    return render(request, 'user/password_success.html', {})