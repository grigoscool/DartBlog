from django import template

from blog.models import Category

register = template.Library()


@register.inclusion_tag('blog/cat_menu.html', takes_context=True)
def get_cat_menu(context, menu_class=None):
    if check_home(str(context['request']).split('/')):
        active_cat = 'home'
    else:
        active_cat = str(context['request']).split('/')[-2]
    cats = Category.objects.all()
    return {'cats': cats, 'menu_class': menu_class, 'active_cat': active_cat}


def check_home(s: list):
    return False if 'category' in s else True
