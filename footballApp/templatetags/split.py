from django import template
register = template.Library()


@register.filter
def split(data, splitter=","):
    return data.split(splitter)
