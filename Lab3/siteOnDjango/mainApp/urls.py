from django.urls import path
from . import views
from django.views.generic import ListView, DetailView
from mainApp.models import Events
from django.contrib.auth import views as auth_views


urlpatterns = [
    # path('events/', ListView.as_view(queryset = Events.objects.all().order_by("-date")[:20], template_name = 'mainApp\events.html')),
    path('events/', views.allEvents, name = 'allEvents'),
    path('', views.index, name='index'),
    path('events/<int:event_id>/', views.detail, name='detail'),
    path('deleteEvent/<int:event_id>/', views.delete, name='delete'),
    path('deleteFollower/<int:event_id>/<int:follower_id>/', views.deleteFollower, name='deleteFollower'),
    # path('addEvent/', views.addEvent, name = 'addEvent'),
    # path('authapp/login/', auth_views.login, name='authapp-login'),
]
