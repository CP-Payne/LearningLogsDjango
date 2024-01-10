"""Defines URL patterns for users"""

from django.urls import path, include

from . import views as custom_views
from django.contrib.auth import views

app_name = 'users'
urlpatterns = [
    # Include default auth urls. (such as login)
    path('', include('django.contrib.auth.urls')),
    # path('login/', views.LoginView.as_view(), name='login'),
    # path('logout/', views.LogoutView.as_view(), name='logout'),
    # Registration page.
    path('register/', custom_views.register, name='register'),
]
