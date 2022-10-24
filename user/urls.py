from django.contrib import admin
from django.urls import path
from . import views

# user/...
urlpatterns = [
    path('profile/', views.user_profile, name='profile'),
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logour/', views.user_logout, name='logout')
]
