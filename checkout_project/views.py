from django.shortcuts import render, HttpResponseRedirect, redirect
from product.models import Message
from django.views.generic import View
from django.http import JsonResponse

# Create your views here.


# Send Message
class send_message(View):
    def get(self, request):
        name = request.GET.get('n', None)
        email = request.GET.get('e', None)
        message = request.GET.get('m', None)

        print(name, email, message)

        done = Message.objects.create(name=name, phone=email, msg=message)

        if done:
            data = 1
        else:
            data = 0

        return JsonResponse(data, safe=False)

        return JsonResponse(room_list, safe=False)
