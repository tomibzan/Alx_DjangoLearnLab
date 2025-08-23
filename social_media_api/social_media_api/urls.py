# social_media_api/urls.py
from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Social Media API",
        default_version='v1',
        description="A full-featured social media API with posts, follows, likes, comments, and notifications",
        contact=openapi.Contact(email="thomflowen@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),    
    public=True,
    permission_classes=(permissions.AllowAny,),
)    
        


def home(request):
    return HttpResponse("Welcome to Social Media API Demonstration by Thomas Seid. Go to /api/accounts/ to register.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/', include('posts.urls')),  # /api/posts/, /api/comments/
    path('api/notifications/', include('notifications.urls')),
    path('', home, name='home'),
    path('api-auth/', include('rest_framework.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
