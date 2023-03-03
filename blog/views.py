from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Post, Category, Tag


class IndexView(generic.ListView):
    """
    Home view - list of posts and main post.
    """
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        return Post.objects.all().order_by('-views').select_related('author')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Classic Blog'
        return context


class PostView(generic.DetailView):
    """
    Show current post.
    """
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()

        context['title'] = context['post'].title
        return context


class PostsByCategory(generic.ListView):
    """
    Show posts list by current category.
    """
    template_name = 'blog/postsByCat.html'
    paginate_by = 4
    allow_empty = False
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(
            category__slug=self.kwargs['slug']).order_by('-views').select_related('author')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['posts'][0].category
        return context


class PostsByTag(generic.ListView):
    """
    Show posts list by current tag.
    """
    template_name = 'blog/postsByTag.html'
    paginate_by = 4
    allow_empty = False
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(
            tag__slug=self.kwargs['slug']).order_by('-views').select_related('author')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Tag.objects.get(slug=self.kwargs['slug'])
        return context


class Search(generic.ListView):
    model = Post
    template_name = 'blog/search.html'
    paginate_by = 1
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Search'
        context['search'] = f"search={self.request.GET.get('search')}&"
        return context

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('search'))
