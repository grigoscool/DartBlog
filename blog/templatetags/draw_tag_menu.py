from django import template

from blog.models import Tag

register = template.Library()


@register.inclusion_tag('blog/tag_menu.html')
def get_tag_menu(cnt=20):
    tags = Tag.objects.all()
    if len(tags) > cnt:
        tags = tags[:cnt]
    return {'tags': tags}
