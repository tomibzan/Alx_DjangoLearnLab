from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Book, Article


class BookForm(forms.ModelForm):
    """
    Form for creating and editing books with proper validation
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Enter book title')
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Enter author name')
            }),
            'publication_year': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': _('Enter publication year')
            }),
        }
        labels = {
            'title': _('Book Title'),
            'author': _('Author'),
            'publication_year': _('Publication Year'),
        }

    def clean_publication_year(self):
        """Validate publication year to prevent invalid data"""
        year = self.cleaned_data['publication_year']
        if year and (year < 0 or year > 2024):
            raise forms.ValidationError(
                _("Please enter a valid publication year."))
        return year

    def clean_title(self):
        """Clean and validate title field"""
        title = self.cleaned_data['title']
        if title and len(title.strip()) == 0:
            raise forms.ValidationError(_("Title cannot be empty."))
        return title.strip()

    def clean_author(self):
        """Clean and validate author field"""
        author = self.cleaned_data['author']
        if author and len(author.strip()) == 0:
            raise forms.ValidationError(_("Author cannot be empty."))
        return author.strip()


class ArticleForm(forms.ModelForm):
    """
    Form for creating and editing articles with proper validation
    """
    class Meta:
        model = Article
        fields = ['title', 'content', 'published']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Enter article title')
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
                'placeholder': _('Enter article content')
            }),
            'published': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
        labels = {
            'title': _('Article Title'),
            'content': _('Content'),
            'published': _('Published'),
        }

    def clean_title(self):
        """Clean and validate title field"""
        title = self.cleaned_data['title']
        if title and len(title.strip()) == 0:
            raise forms.ValidationError(_("Title cannot be empty."))
        return title.strip()

    def clean_content(self):
        """Clean and validate content field"""
        content = self.cleaned_data['content']
        if content and len(content.strip()) == 0:
            raise forms.ValidationError(_("Content cannot be empty."))
        return content.strip()


class BookSearchForm(forms.Form):
    """
    Form for searching books with proper validation
    """
    query = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Search books by title or author...'),
            'aria-label': _('Search')
        }),
        label=_('Search Query')
    )

    def clean_query(self):
        """Clean search query"""
        query = self.cleaned_data['query']
        return query.strip() if query else query


class ExampleForm(forms.Form):
    """
    Example form demonstrating various field types and validation
    This form is for demonstration purposes and can be used for testing
    """
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Enter your name')
        }),
        label=_('Name'),
        help_text=_('Please enter your full name')
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': _('Enter your email')
        }),
        label=_('Email Address'),
        help_text=_('We will never share your email')
    )

    age = forms.IntegerField(
        min_value=1,
        max_value=120,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': _('Enter your age')
        }),
        label=_('Age'),
        help_text=_('Must be between 1 and 120')
    )

    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': _('Enter your message')
        }),
        label=_('Message'),
        required=False
    )

    subscribe = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        }),
        label=_('Subscribe to newsletter'),
        help_text=_('Check this box to receive our newsletter')
    )

    def clean_name(self):
        """Validate name field"""
        name = self.cleaned_data['name']
        if len(name.strip()) < 2:
            raise forms.ValidationError(
                _("Name must be at least 2 characters long."))
        return name.strip()

    def clean_email(self):
        """Validate email field"""
        email = self.cleaned_data['email']
        # Additional email validation can be added here
        return email.lower()

    def clean(self):
        """Cross-field validation"""
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')

        # Example of cross-field validation
        if name and email and name.lower() in email.lower():
            raise forms.ValidationError(
                _("Name should not be part of email address."))

        return cleaned_data
