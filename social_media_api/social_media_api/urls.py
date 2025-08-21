# social_media_api/urls.py
from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Social Media API. Go to /api/accounts/ to register.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/', include('posts.urls')),  # /api/posts/, /api/comments/
    path('api/notifications/', include('notifications.urls')),
    path('', home),
]
