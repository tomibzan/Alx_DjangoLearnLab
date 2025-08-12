from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    """
    Represents a blog post.
    Each post has a title, content, author, and publication date.
    """
    title = models.CharField(max_length=200, help_text="Enter the post title")
    content = models.TextField(help_text="Write your blog content here")
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        help_text="The user who wrote this post"
    )

    def __str__(self):
        return self.titles

    class Meta:
        ordering = ['-published_date']  # Newest first

    def get_absolute_url(self):
        """Optional: used for redirect after create/update"""
        return reverse('post-detail', kwargs={'pk': self.pk})
