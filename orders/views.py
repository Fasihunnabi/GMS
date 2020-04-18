from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse, HttpResponseRedirect
from product.models import Product
from orders.models import OrderDetail, Order
from .forms import OrderForm

# Create your views here.


class cart(View):
    def get(self, request):
        to_dump = []
        id = request.GET.get('p_id', None)  # Getting the product id

        # Check if some product ids are already stored in session
        # If yes, then update the to_dump list with them
        try:
            if request.session['product_ids']:
                previous_cart_items = request.session['product_ids']
                to_dump = previous_cart_items
                #print("Already Stored Ids: ", to_dump)
        except:
            pass

        # Append a new id to the to_dump list
        to_dump.append(id)

        # Remove duplicate ids from the list
        items_ids_list = list(dict.fromkeys(to_dump))

        # Update the session with the new list
        request.session['product_ids'] = items_ids_list
        new_cart_list = request.session['product_ids']
        # print("New is, ", new_cart_list)

        if new_cart_list:
            data = 1
        else:
            data = 0

        # del request.session['product_ids']

        return JsonResponse(data, safe=False)


class delete_item_from_cart(View):
    def get(self, request):
        to_dump = []
        id = request.GET.get('p_id', None)  # Getting the product id

        # Check if some product ids are already stored in session
        # If yes, then update the to_dump list with them
        try:
            if request.session['product_ids']:
                previous_cart_items = request.session['product_ids']
                to_dump = previous_cart_items
                #print("Already Stored Ids: ", to_dump)
        except:
            pass

        # Remove duplicate ids from the list
        items_ids_list = list(dict.fromkeys(to_dump))

        # Delete a product id from to_dump list
        items_ids_list.remove(id)

        # Update the session with the new list
        request.session['product_ids'] = items_ids_list
        new_cart_list = request.session['product_ids']
        # print("New is, ", new_cart_list)

        if new_cart_list:
            data = 1
        else:
            data = 0

        # del request.session['product_ids']

        return JsonResponse(data, safe=False)


def order_finalize(request):
    er_message = ''

    try:
        ids_list = request.session['product_ids']
        products_list = Product.objects.filter(id__in=ids_list)
    except:
        products_list = []

    form = OrderForm(request.POST or None, request.FILES or None)

    if request.POST:
        print("It came in post request")
        print(request.POST)
        form = OrderForm(request.POST)
        print(form)
        print(form.errors)
        if form.is_valid():
            print("valid form")
            order_object = form.save()
            print("It came in request post")
            print(request.POST)

            id = request.POST.getlist('productID', None)
            price = request.POST.getlist('productSalePrice', None)
            qty = request.POST.getlist('productQuantity', None)
            total_sum = request.POST.getlist('productTotalSum', None)
            objects_list = zip(id, price, qty, total_sum)  # Zip the information in an object
            total_order_cost = 0

            for i in objects_list:
                product_object = Product.objects.get(id=i[0])
                print(i[0], i[1], i[2], i[3])
                order_detail_object = OrderDetail.objects.create(product=product_object,
                                                                 order_detail_sku=product_object.sku,
                                                                 order_detail_quantity=i[2], order_detail_price=i[3])
                order_object.order_detail.add(order_detail_object)
                total_order_cost = total_order_cost + int(i[3])

            new_obj = Order.objects.get(id=order_object.id)
            new_obj.order_cost = total_order_cost
            new_obj.save()

            del request.session['product_ids']

            return HttpResponseRedirect("/order/order-placed-successfully/" + str(order_object.id) + "?done=true")

        else:
            print(form.errors)
            er_message = form.errors


    context = {
        'products_list': products_list,
        'form': form,
        'er_message': er_message
    }

    return render(request, "finalize_order.html", context)


def order_placed_successfully(request, slug):

    order_object = Order.objects.get(id=slug)

    context = {
        'order_object': order_object
    }

    return render(request, "order_success.html", context)
