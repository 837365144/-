from django import template

register = template.Library()

@register.filter
def div(v1,v2):
    return round(v1/v2*10,2)