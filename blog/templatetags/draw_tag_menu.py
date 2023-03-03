from django import template

from blog.models import Tag

register = template.Library()


@register.inclusion_tag('blog/tag_menu.html')
def get_tag_menu():
    tags = Tag.objects.all()
    return {'tags': tags}
