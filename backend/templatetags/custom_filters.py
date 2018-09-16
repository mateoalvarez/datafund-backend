from django import template

register = template.Library()


@register.filter(name="next_value")
def next_value(iterator):
    """Returns next value of an iterator inside a template as a filter"""
    return next(iterator)
