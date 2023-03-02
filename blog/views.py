from django.shortcuts import render
from django.views import generic

from .models import Post


# def index(request):
#     return render(request, 'blog/index.html')

class IndexView(generic.ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Classic Blog'
        return context

def show_cat(request, slug):
    return render(request, 'blog/cat.html')
