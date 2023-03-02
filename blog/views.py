from django.shortcuts import render
from django.views import generic

from .models import Post


class IndexView(generic.ListView):
    """
    Home view - list of posts and main post.
    """
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Classic Blog'
        return context


class PostView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


def show_cat(request, slug):
    return render(request, 'blog/cat.html')
