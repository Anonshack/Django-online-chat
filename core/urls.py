from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import UserListView, PasswordChangeView, password_success

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('list-users/', UserListView.as_view(), name='users-list'),
    path('password/', PasswordChangeView.as_view(template_name='user/change-password.html'), name='password-change'),
    path("password/success", password_success, name="password-success"),
]