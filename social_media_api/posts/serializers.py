# posts/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post, Comment

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')
    author_first_name = serializers.ReadOnlyField(source='author.first_name')
    author_last_name = serializers.ReadOnlyField(source='author.last_name')

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'content',
            'author_username', 'author_first_name', 'author_last_name',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['author']  # Set in view


class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = [
            'id', 'content', 'author_username', 'created_at', 'updated_at', 'post'
        ]
        read_only_fields = ['author', 'post']