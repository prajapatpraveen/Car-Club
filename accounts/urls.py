from django import views
from django.urls import path
from . import views
urlpatterns=[
    path('login',views.Login, name='login'),
    path('register',views.Register, name='register'),
    path('logout',views.Logout, name='logout'),
    path('dashboard',views.Dashboard, name='dashboard'),
    
]