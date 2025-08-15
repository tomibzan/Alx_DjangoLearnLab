# blog/models.py
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

class Post(models.Model):
    """Represents a blog post."""
    title = models.CharField(max_length=200, help_text="Enter the post title")
    content = models.TextField(help_text="Write your blog content here")
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
        help_text="The user who wrote this post",
    )
    tags = TaggableManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-published_date"]

    def get_absolute_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.pk})

class Comment(models.Model):
    """Represents a comment on a blog post."""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField(help_text="Write your comment here")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"

    class Meta:
        ordering = ["-created_at"]
