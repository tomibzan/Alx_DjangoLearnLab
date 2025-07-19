from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator


# Define Role choices
ROLE_CHOICES = [
    ('Admin', 'Admin'),
    ('Librarian', 'Librarian'),
    ('Member', 'Member'),
]


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='Member'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"


# Signal to handle UserProfile creation/updates
@receiver(post_save, sender=User)
def handle_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    elif hasattr(instance, 'userprofile'):
        instance.userprofile.save()


# Assign user to Group based on role
@receiver(post_save, sender=UserProfile)
def assign_role_group(sender, instance, **kwargs):
    group, _ = Group.objects.get_or_create(name=instance.role)
    instance.user.groups.add(group)


class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'
    )
    publication_year = models.IntegerField(
        validators=[
            MinValueValidator(1000),
            MaxValueValidator(2025)
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"


class Library(models.Model):
    name = models.CharField(max_length=100, unique=True)
    books = models.ManyToManyField(
        Book,
        related_name='libraries',
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Librarian(models.Model):
    user_profile = models.OneToOneField(
        UserProfile,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'Librarian'}
    )
    library = models.ForeignKey(
        Library,
        on_delete=models.CASCADE,
        related_name='librarians'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user_profile.user.username} ({self.library.name})"
