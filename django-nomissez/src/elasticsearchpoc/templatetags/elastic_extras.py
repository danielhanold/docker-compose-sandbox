from django import template

register = template.Library()

@register.filter()
def get_underscore(value, arg):
    """Removes all values of arg from the given string"""
    return value.get(arg, None)



