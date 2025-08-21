# accounts/urls.py
from django.urls import path
from . import views
from .views import RegisterView, LoginView, ProfileView, FollowUserView, UnfollowUserView, UserListView
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    # Follow/unfollow endpoints
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
    path('users/', UserListView.as_view(), name='user-list'),
]