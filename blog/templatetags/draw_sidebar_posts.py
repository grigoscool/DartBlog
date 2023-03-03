from django import template

from blog.models import Post

register = template.Library()


@register.inclusion_tag('blog/sidebar_posts.html', takes_context=True)
def get_sidebar_posts(context, cnt=3):
    order = context['request'].GET
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


