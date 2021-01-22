from django import template

register = template.Library()

# annotation을 적용하면 템플릿에서 해당 함수를 필터로 사용할 수 있게 됨
@register.filter
def sub(value, arg):
    return value - arg