from django.urls import path
from . import views

urlpatterns = [
     path('post_event/', views.post_event, name='post_event'),
]