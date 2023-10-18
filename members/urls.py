from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='members-home'),
    path('members/send_push_notification/',  views.send_push_notification, name='send_push_notification'),
]