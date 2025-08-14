# blog/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = "blog"

urlpatterns = [
    # Blog
    path("", views.PostListView.as_view(), name="post-list"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("post/new/", views.PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update/", views.PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post-delete"),

    # Auth
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),  # uses LOGOUT_REDIRECT_URL setting

    # Profile
    path("profile/", views.profile, name="profile"),
    path("profile/edit/", views.edit_profile, name="edit_profile"),

    path('posts/<int:post_id>/comments/add/', views.add_comment, name='add_comment'),
    path('comments/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]
