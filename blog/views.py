from django.shortcuts import render
from django.views import generic

from .models import Post, Category


class IndexView(generic.ListView):
    """
    Home view - list of posts and main post.
    """
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        return Post.objects.all().select_related('author')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Classic Blog'
        return context


class PostView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class PostsByCategory(generic.ListView):
    """
    Show posts list by current category.
    """
    model = Post
    template_name = 'blog/postsByCat.html'
    paginate_by = 4
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(
            category__slug=self.kwargs['slug']).select_related('author')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # takes category title into page title
        if len(context['posts']) > 0:
            context['title'] = context['posts'][0].category
        return context
