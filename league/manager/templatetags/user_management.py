from django import template
register = template.Library()


@register.filter
def is_judge(user):
    return user.groups.filter(name="Judges").exists()
