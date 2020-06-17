from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from . import views
app_name='bauth'
urlpatterns = [
    path('',views.home,name='home'),
    path('login/',auth_views.LoginView.as_view(template_name='bauth/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='bauth/logout.html'),name='logout'),
    
    path('register/',views.register,name='register'),
]
