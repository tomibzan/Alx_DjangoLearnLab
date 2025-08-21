# posts/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post, Comment

User = get_user_model()

class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for Post model.
    Exposes author details without allowing modification.
    """
    author_username = serializers.CharField(source='author.username', read_only=True)
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'author_username',
            'author_first_name',
            'author_last_name',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']

    def validate_title(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long.")
        return value

    def validate_content(self, value):
        if len(value.strip()) < 1:
            raise serializers.ValidationError("Content cannot be empty.")
        return value

class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for Comment model.
    Author and post are set server-side; not user-editable.
    """
    author_username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Comment
        fields = [
            'id',
            'post',
            'author_username',
            'content',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['author', 'post', 'created_at', 'updated_at']

    def validate_content(self, value):
        if len(value.strip()) < 1:
            raise serializers.ValidationError("Comment cannot be empty.")
        return value
