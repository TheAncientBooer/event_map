from django.contrib import admin
from map import views as map_views
from django.urls import path, include
from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', map_views.index, name='index'),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('', include('map.urls')),
] 
