# blog/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post, Comment
from .forms import PostForm, CommentForm

# ----- Auth -----


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['post_id']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.kwargs['post_id']})


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['content']

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.id})


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.id})
    
class CustomUserCreationForm(UserCreationForm):
    """Extend the stock form to require email."""
    class Meta:
        model = get_user_model()
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get("email", "")
        if commit:
            user.save()
        return user

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("blog:post-list")
    else:
        form = CustomUserCreationForm()
    return render(request, "blog/register.html", {"form": form})


@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.success(request, 'Your comment has been added.')
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form})


@login_required
def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user != comment.author:
        messages.error(request, 'You are not authorized to edit this comment.')
        return redirect('post_detail', pk=comment.post.pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your comment has been updated.')
            return redirect('post_detail', pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'blog/comment_form.html', {'form': form})


@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user != comment.author:
        messages.error(request, 'You are not authorized to delete this comment.')
        return redirect('post_detail', pk=comment.post.pk)

    if request.method == 'POST':
        comment.delete()
        messages.success(request, 'Your comment has been deleted.')
        return redirect('post_detail', pk=comment.post.pk)

    return render(request, 'blog/comment_confirm_delete.html', {'comment': comment})
# ----- Blog -----
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    ordering = ["-published_date"]
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    # Provide a comment form on the detail page
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["comment_form"] = CommentForm()
        return ctx

    # Handle comment submission on the same URL
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not request.user.is_authenticated:
            return redirect("blog:login")
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                post=self.object,
                author=request.user,
                content=form.cleaned_data["content"],
            )
            return redirect("blog:post-detail", pk=self.object.pk)
        ctx = self.get_context_data()
        ctx["comment_form"] = form
        return render(request, self.template_name, ctx)
    
    def post_detail(request, pk):
        post = get_object_or_404(Post, pk=pk)
        comment_form = CommentForm()
        return render(request, 'blog/post_detail.html', {
        'post': post,
        'comment_form': comment_form
    })


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("blog:post-detail", kwargs={"pk": self.object.pk})

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("blog:post-detail", kwargs={"pk": self.object.pk})

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("blog:post-list")

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# Optional redirect if you ever want a separate "home"
def home(request):
    return redirect("blog:post-list")
