from django import template
from exam.models import *

register = template.Library()

@register.filter
def getch(ch_id):
    return Choice.objects.get(id=ch_id)


@register.filter
def checked(ch):
    return ch['choice']