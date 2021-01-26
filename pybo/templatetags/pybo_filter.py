import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

# annotation을 적용하면 템플릿에서 해당 함수를 필터로 사용할 수 있게 됨
@register.filter
def sub(value, arg):
    return value - arg


@register.filter
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))
