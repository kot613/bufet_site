from django import template
from blog.models import Category, Comment
from django.db.models import Count

register = template.Library()

@register.inclusion_tag('blog/inc/tags/side_menu.html')
def get_categories():
    # category = Category.objects.order_by('name')
    category = Category.objects.annotate(cnt=Count('post')).order_by('-cnt')
    return {'list_category': category}


@register.inclusion_tag('blog/inc/tags/comment_karusel.html')
def get_comments():
    # category = Category.objects.order_by('name')
    comment = Comment.objects.all()[:5]
    return {'list_comment': comment}

