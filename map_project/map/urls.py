from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
     path('post_event/', views.post_event, name='post_event'),
]

urlpatterns += staticfiles_urlpatterns()