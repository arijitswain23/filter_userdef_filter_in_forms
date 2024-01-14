from django import template
register=template.Library()


def swap(value):
    return value.swapcase()


def remove(value,arg):
    return value.replace(arg,'')


@register.filter()
def counting(value,ele):
    return value.count(ele)












register.filter('swapping',swap)
register.filter('removing',remove)
#register.filter('counting',count)
