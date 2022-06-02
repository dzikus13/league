from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
def is_judge(user):
    return user.groups.filter(name="Judges").exists()


@register.filter(name='group')
def group(u, group_names):
    return u.groups.filter(name=group_names)
