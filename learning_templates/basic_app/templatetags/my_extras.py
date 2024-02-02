from django import template

register = template.Library()

@register.filter(name='cut') #learn python decorators
def cut(value,arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')

# register.filter('cut',cut)