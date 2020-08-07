from django import template

register = template.Library()
#option 2 using decoratorss
@register.filter(name='cut')

def cut(value,arg):
    """this cuts out all values of "arg" from string"""

    return value.replace(arg)
#option 1
#first cut the one we call in templatagg
#register.filter('cut',cut)
