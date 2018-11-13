from django.urls import path
from . import views
from django.views.generic import ListView, DetailView
from mainApp.models import Events


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
