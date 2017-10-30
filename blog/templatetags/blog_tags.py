from ..models import Category,Tag,Post
from django import template
from django.db.models.aggregates import Count

register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-create_time')[:num]

@register.simple_tag
def archives():
    return Post.objects.dates('create_time','month',order='DESC')

@register.simple_tag
def get_categories():
    # return Category.objects.all()
    return Category.objects.annotate(post_num=Count('post')).filter(post_num__gt=0)
