from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from orders.models import Order
from product.models import Message, ProductCategory, Product, ProductImage
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import logout as Logout
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from product.forms import *
from django.views.generic import View
from django.http import JsonResponse
from django.contrib.auth.models import User


# Create your views here.


def login(request):
    template_name = "superadmin/login.html"
    error = None
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            email = data["username"]
            password = data["password"]
            try:
                try:
                    user = User.objects.get(email__iexact=email)
                except Exception as e:
                    print('Exception', e)
                    user = User.objects.get(username__iexact=email)
                if user.check_password(password):
                    user_auth = authenticate(username=user.username, password=password)
                    print("asd", user)
                    auth_login(request, user_auth)
                    return HttpResponseRedirect('/')
                else:
                    error = "invalid Email or Password"

            except Exception as e:
                print(e)
                error = "invalid Email or Password"
        else:
            print(form.errors)
            error = form.errors
    context = {
        'form': form,
        'error': error,
    }
    return render(request, template_name, context)


def logout(request):
    Logout(request)
    return HttpResponseRedirect('/login/')


def view_employee(request):
    su_message = request.GET.get("message")
    print(su_message)

    employee_list = Employee.objects.filter(emp_supervisor=request.user)

    context = {
        'su_message': su_message,
        'employee_list': employee_list,
    }

    return render(request, "superadmin/Employee/list_employee.html", context)


def add_employee(request):
    su_message = request.GET.get("message")
    user_form = user_register_form(request.POST or None)
    form = Employee_form(request.user, request.POST or None)

    if request.POST:
        # print("It came in post request")
        print(form)
        print(form.errors)
        if user_form.is_valid():
            user_obj = user_form.save()
            if form.is_valid():
                print("valid form")
                form_obj = form.save(commit=False)
                form_obj.emp_User = user_obj
                form_obj.emp_supervisor = request.user
                form_obj.save()
                return HttpResponseRedirect("/employee?message=success")
            else:
                print(form.errors)

    context = {
        'form': form,
        'register_form': user_form,
    }

    return render(request, "superadmin/Employee/add_employee.html", context)


def edit_employee(request, id):
    su_message = request.GET.get("message")
    emp_obj = Employee.objects.get(id=id)
    user_form = user_update_form(request.POST or None, instance=emp_obj.emp_User)
    form = Employee_form(request.user, request.POST or None, instance=emp_obj)
    print("Update Employee")
    if request.POST:
        print("Update Employee")
        if form.is_valid():
            print("employeedate valid form")
            form.save()
        else:
            print(form.errors)
        if user_form.is_valid():
            user_form.save()
        else:
            print(user_form.errors)

        return HttpResponseRedirect("/employee?message=success")
    context = {
        'form': form,
        'register_form': user_form,
        'status': 'update'
    }

    return render(request, "superadmin/Employee/add_employee.html", context)


class delete_employee(View):
    def get(self, request):

        emp_id = request.GET.get('id', None)

        res = Employee.objects.get(id=emp_id).delete()

        isSuccess = []
        if (res):
            print("order  dellllllllllllllllllllllllllllllllllll")
            isSuccess.append("deleted")
        else:
            isSuccess.append("not deleted")

        return JsonResponse(isSuccess, safe=False)


def add_device(request):
    er_message = ''
    form = DeviceForm(request.POST or None)

    if request.POST:
        # print("It came in post request")
        print(form)
        print(form.errors)
        if form.is_valid():
            print("valid form")
            form_obj = form.save(commit=False)
            form_obj.Engine_supervisor = request.user
            form_obj.save()
            return HttpResponseRedirect("/view-devices?message=success")
        else:
            print(form.errors)
            er_message = form.errors

    context = {
        'form': form,
        'er_message': er_message
    }

    return render(request, "superadmin/add_engine.html", context)


def edit_device(request, id):
    er_message = ''

    device_object = Device.objects.get(id=id)
    form = DeviceForm(request.POST or None, instance=device_object)

    if request.POST:
        if form.is_valid():
            form_obj = form.save(commit=False)
            print("valid form")
            form_obj.save()
            return HttpResponseRedirect("/view-devices?message=update-success")

        else:
            print(form.errors)
            er_message = form.errors

    context = {
        'form': form,
        'status': 'updatepage',
        'er_message': er_message
    }

    return render(request, "superadmin/add_engine.html", context)


class deletedevice(View):
    def get(self, request):

        p_id = request.GET.get('id', None)

        res = Device.objects.get(id=p_id).delete()
        isSuccess = []

        if (res):
            print("dellllllllllllllllllllllllllllllllllll")
            isSuccess.append("deleted")
        else:
            isSuccess.append("not deleted")

        return JsonResponse(isSuccess, safe=False)


def view_devices(request):
    su_message = request.GET.get("message")
    engine_list = Device.objects.filter(Engine_supervisor=request.user)

    context = {
        'su_message': su_message,
        'engine_list': engine_list
    }

    return render(request, "superadmin/viewengines.html", context)


def add_sensor(request):
    er_message = ''

    form = Sensor_form(request.user, request.POST or None)
    if request.POST:

        if form.is_valid():
            print("valid form")
            form.save()

            return HttpResponseRedirect("/view-sensor?message=success")
        else:
            print(form.errors)
            er_message = form.errors

    context = {
        'form': form,
        'er_message': er_message
    }

    return render(request, "superadmin/sensors/add_sensor.html", context)


def edit_sensor(request, id):
    er_message = ''

    sensor_object = Sensors.objects.get(id=id)
    form = Sensor_form(request.user, request.POST or None, instance=sensor_object)

    if request.POST:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/view-sensor?message=update-success")

        else:
            print(form.errors)
            er_message = form.errors

    context = {
        'form': form,
        'status': 'updatepage',
        'er_message': er_message
    }

    return render(request, "superadmin/sensors/add_sensor.html", context)


class deletesensor(View):
    def get(self, request):

        p_id = request.GET.get('id', None)

        res = Sensors.objects.get(id=p_id).delete()
        isSuccess = []

        if (res):
            print("dellllllllllllllllllllllllllllllllllll")
            isSuccess.append("deleted")
        else:
            isSuccess.append("not deleted")

        return JsonResponse(isSuccess, safe=False)


def view_sensor(request):
    su_message = request.GET.get("message")
    sensor_list = Sensors.objects.filter(device__Engine_supervisor=request.user)

    context = {
        'su_message': su_message,
        'sensor_list': sensor_list
    }

    return render(request, "superadmin/sensors/list_sensors.html", context)
