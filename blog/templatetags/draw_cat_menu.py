from django import template

from blog.models import Category

register = template.Library()


@register.inclusion_tag('blog/cat_menu.html')
def get_cat_menu(menu_class=None):
    cats = Category.objects.all()
    return {'cats': cats, 'menu_class': menu_class}