from django import template
import random

from blog.models import Post

register = template.Library()


@register.inclusion_tag('blog/sidebar_posts.html', takes_context=True)
def get_sidebar_posts(context, cnt=3):
    # Take posts list for sidebar
    order = context['request'].GET
    # Takes random post list if no get request
    if len(order) == 0:
        posts_id = Post.objects.all().values_list('pk', flat=True)
        random_posts_id = random.sample(sorted(posts_id), k=3)
        sidebar_posts = Post.objects.filter(pk__in=random_posts_id)
        return {'sidebar_posts': sidebar_posts}
    else:
        for i in order:
            if i == 'recent':
                sidebar_posts = Post.objects.all().order_by('-create_at')[:cnt]
                return {'sidebar_posts': sidebar_posts}
            elif i == 'popular':
                sidebar_posts = Post.objects.all().order_by('-views')[:cnt]
                return {'sidebar_posts': sidebar_posts}
            elif i == 'user':
                sidebar_posts = Post.objects.all().order_by('author')[:cnt]
                return {'sidebar_posts': sidebar_posts}


