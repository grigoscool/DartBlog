from django import template
from django.core.cache import cache
from blog.models import Category

register = template.Library()


@register.inclusion_tag('blog/cat_menu.html', takes_context=True)
def get_cat_menu(context, menu_class=None):
    """
    Draw category list in navbar and footer.
    :param context:
    :param menu_class: style class of container
    :return: queryset dict of category
    """
    # check active home page or category
    if check_home(str(context['request']).split('/')):
        active_cat = 'home'
    else:
        active_cat = str(context['request']).split('/')[-2]
    # cache category queryset to only 1 sql
    cats = cache.get('cats')
    if not cats:
        cats = Category.objects.all()
        cache.set('cats', cats, 30)
    return {'cats': cats, 'menu_class': menu_class, 'active_cat': active_cat}


def check_home(s: list):
    return False if 'category' in s else True

