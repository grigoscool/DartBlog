from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.db.models import F
from django.views import generic
from django.shortcuts import render, redirect

from .models import Post, Tag
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm

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
    """
    Show page with search result.
    """
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


def login(request):

    return render(request, 'blog/login.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'УРА')
            return redirect('login')
        else:
            messages.error(request, 'NOT RIGHT')
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form})


# class Register(generic.CreateView):
#     model = User
#     form_class = UserCreationForm
#     template_name = 'blog/register.html'
#     context_object_name = 'form'
