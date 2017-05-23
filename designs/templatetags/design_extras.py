from django import template
from django.utils.safestring import mark_safe
import markdown2

register = template.Library()

@register.filter(name='img_src')
def img_src(value):
    value = str(value)
    value = value.split("/")[1:]
    return '/'.join(value)

@register.filter(name="add_id")
def add_id(value):
    return "#" + str(value)

@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
    '''Converts markdown text to HTML '''   
    html_body = markdown2.markdown(markdown_text)
    return mark_safe(html_body)

@register.filter('path_single')
def path_single(main_path):
    '''Gets main path of url path'''
    return main_path.split('/')[1]

@register.filter(name="month_finder")
def month_finder(value):
    if value == 1:
        return "January"
    elif value == 2:
        return "February"
    elif value == 3:
        return "March"
    elif value == 4:
        return "April"
    elif value == 5:
        return "May"
    elif value == 6:
        return "June"
    elif value == 7:
        return "July"
    elif value == 8:
        return "August"
    elif value == 9:
        return "September"
    elif value == 10:
        return "October"
    elif value == 11:
        return "November"
    else:
        return "December"