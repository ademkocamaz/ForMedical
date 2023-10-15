from django import template
from multipledispatch import dispatch

register = template.Library()

@register.simple_tag()
def verbose_name(instance):
    """Returns the verbose_name of the specified field."""
    return instance._meta.verbose_name.title()

@register.simple_tag()
def verbose_name_plural(instance):
    """Returns the verbose_name_plural of the specified field."""
    return instance._meta.verbose_name_plural.title()

@register.simple_tag()
def field_verbose_name(instance, field_name):
    """Returns the verbose_name of the specified field."""
    return instance._meta.get_field(field_name).verbose_name.title()
