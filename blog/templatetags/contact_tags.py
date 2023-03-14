from django import template
from blog.forms import EmailForm

register = template.Library()


@register.inclusion_tag('blog/inc/tags/_email_form.html')
def email_form():
    return {'email_form': EmailForm()}
