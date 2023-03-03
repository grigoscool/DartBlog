from django import template

from blog.models import Post

register = template.Library()



@register.inclusion_tag('blog/button_group.html')
def get_button_group(cnt=3):
    posts_recent = Post.objects.all().order_by('-create_at').select_related('author')[:cnt]
    return {'posts_recent': posts_recent}
