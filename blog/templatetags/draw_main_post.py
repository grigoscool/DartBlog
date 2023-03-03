from django import template

from blog.models import Post

register = template.Library()


@register.inclusion_tag('blog/main_post.html')
def get_main_post():
    """
    Show main post on index.html
    :return: main post
    """
    main_post = Post.objects.get(is_main=True)
    return {'main_post': main_post}
