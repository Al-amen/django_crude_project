from django import template

register = template.Library()


def my_filter(value, arg):
    
    list = []
    for i in value:
        if i %arg == 0:
            list.append(i*i)
    return list

register.filter('custom_filter',my_filter)




