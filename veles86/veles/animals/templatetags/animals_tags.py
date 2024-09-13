from django import template
from animals.models import *

register = template.Library()

# создание пользовательского тега

@register.simple_tag()
def get_images(filter=None):
    if not filter:
        return DogImages.objects.all()
    else:
        return DogImages.objects.filter(subject__pk = filter)


@register.simple_tag()
def get_post_images(filter=None):
    if not filter:
        return PostImages.objects.all()
    else:
        return PostImages.objects.filter(post__pk = filter)