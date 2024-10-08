from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class PasswordChangeingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
