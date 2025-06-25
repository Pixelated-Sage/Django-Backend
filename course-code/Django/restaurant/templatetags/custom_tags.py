from django import template

from django.utils.timezone import now

register = template.Library()   

@register.simple_tag
def current_year():
    current_year = now().year
    if current_year == 2020:
        return "{current_year}"
    else :
        return f"2020 - {current_year} "
