from django.shortcuts import render , HttpResponseRedirect , HttpResponse
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

# def login(request):
#     return render(request, "superadmin/login.html")

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


def view_orders(request):
    su_message = request.GET.get("message")
    print(su_message)

    orders_list = Order.objects.all()

    print(orders_list)

    context = {
        'su_message': su_message,
        'orders_list': orders_list,
    }

    return render(request, "superadmin/orders.html", context)


class deleteOrder(View):
    def get(self, request):

        p_id = request.GET.get('id', None)

        res = Order.objects.get(id=p_id).delete()

        isSuccess = []

        if (res):
            print("order  dellllllllllllllllllllllllllllllllllll")
            isSuccess.append("deleted")
        else:
            isSuccess.append("not deleted")

        return JsonResponse(isSuccess, safe=False)


class StatusAcknowledged(View):
    def get(self, request):

        o_id = request.GET.get('id', None)

        order_object = Order.objects.get(id=o_id)
        order_object.status = "acknowledged"
        res = order_object.save()

        isSuccess = []

        if (res):
            isSuccess.append("status changed")
        else:
            isSuccess.append("not changed")

        return JsonResponse(isSuccess, safe=False)


class StatusDeleivered(View):
    def get(self, request):

        o_id = request.GET.get('id', None)

        order_object = Order.objects.get(id=o_id)
        order_object.status = "deleivered"
        res = order_object.save()

        isSuccess = []

        if (res):
            isSuccess.append("status changed")
        else:
            isSuccess.append("not changed")

        return JsonResponse(isSuccess, safe=False)


def view_messages(request):

    messages_list = Message.objects.all()

    print(messages_list)

    context = {
        'messages_list': messages_list,
    }

    return render(request, "superadmin/messages.html", context)


def add_device(request):
    er_message = ''
    form = DeviceForm(request.POST or None)

    if request.POST:
        print("It came in post request")
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


def product_images(request, slug):

    su_message = request.GET.get("message")
    print(su_message)

    product_object = Product.objects.get(sku=slug)

    img = ProductImage.objects.filter(Product=product_object)
    print(img)
    print(img)
    print(img)
    print(img)
    print(img)

    if request.method == 'POST':
        # Iterate over all the images came in request and add one by one
        for img_obj in request.FILES.getlist('product_images'):
            ProductImage.objects.create(Product=product_object, image=img_obj)


        return HttpResponseRedirect(request.path + '?message=new-images-added-successfully')

    # print(room_object.roomimages_set.all())  # This is how you reverse query

    context = {

        'su_message': su_message,

        'product_object': product_object

    }

    return render(request, "superadmin/product_images.html", context)


def del_product_image(request, slug):

    product_image_object = ProductImage.objects.get(id=slug)
    product_sku = product_image_object.Product.sku
    ProductImage.objects.get(id=slug).delete()

    print(product_sku)
    print(product_sku)
    print(product_sku)
    print(product_sku)
    print(product_sku)

    return HttpResponseRedirect("/product-images/" + str(product_sku) +"?message=image-deleted-successfully")


def del_all_product_images(request, slug):

    product_obj = Product.objects.get(id=slug)

    ProductImage.objects.filter(Product=product_obj).delete()
    return HttpResponseRedirect("/product-images/" + str(product_obj.sku) +"?message=images-deleted-successfully")



