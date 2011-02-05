from django import template
from html_blocks.models import *

register = template.Library()

@register.simple_tag
def html_block(block_position):
    try:
        block=html_block.objects.get(position=block_position)
        return block.content
    except Module.DoesNotExist:
        return block_position+" "+_("module_not_found")