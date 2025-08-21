# posts/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import PostListCreateView, PostDetailView, CommentListCreateView, CommentDetailView, FeedView, LikePostView, UnlikePostView

router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='post')
router.register(r'comments', views.CommentViewSet, basename='comment')

urlpatterns = [
    path("", include(router.urls)),
    path("", PostListCreateView.as_view(), name="post-list-create"),
    path("<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("<int:post_id>/comments/", CommentListCreateView.as_view(), name="comment-list-create"),
    path("comments/<int:pk>/", CommentDetailView.as_view(), name="comment-detail"),
    path("feed/", FeedView.as_view(), name="feed"), 
    path('posts/<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
]
