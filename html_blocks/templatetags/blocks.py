from django import template
from html_blocks.models import *
from django.utils.translation import ugettext as _

register = template.Library()

@register.simple_tag
def html(block_position):
    try:
        block=html_block.objects.get(position=block_position)
        return block.content
    except html_block.DoesNotExist:
        return block_position+" "+_("html block not found")