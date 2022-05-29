from django import template
from blog.models import Category
from django.db.models import Count

register = template.Library()

@register.inclusion_tag('blog/inc/tags/side_menu.html')
def get_categories():
    # category = Category.objects.order_by('name')
    category = Category.objects.annotate(cnt=Count('post')).order_by('-cnt')
    return {'list_category': category}

