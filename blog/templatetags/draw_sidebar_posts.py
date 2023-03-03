from django import template

from blog.models import Post

register = template.Library()


@register.inclusion_tag('blog/sidebar_posts.html', takes_context=True)
def get_sidebar_posts(context, cnt=3):
    order = context['request'].GET
    sidebar_posts = Post.objects.all()[:cnt]
    return {'sidebar_posts': sidebar_posts}
