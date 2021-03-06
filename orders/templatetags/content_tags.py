from django import template
register = template.Library()
from product.models import *


@register.filter(name='is_employee')
def is_employee(id):

    print(id)
    if Employee.objects.filter(emp_User=id)[:1].exists():
        print("id existed")
        return False
    else:
        # if User.objects.filter(username='admin').exists() or User.objects.filter(username='localgms').exists():
        return True

@register.filter(name='formattr')
def attr(obj, arg1):
    att, value = arg1.split("=")
    obj.field.widget.attrs[att] = value
    return obj
