"""coconut URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [

    url(r'^login/$', views.login, name="login"),
    url(r'^logout/$', views.logout, name="logout"),

    path('', login_required(TemplateView.as_view(template_name='superadmin/index.html'), login_url="/login/")),  #After Login yahan redirect krna

    path('employee', login_required(views.view_employee, login_url="/login/")),  # View Orders
    path('add-employee/', login_required(views.add_employee, login_url="/login/")),
    path('edit-employee/<slug:id>', login_required(views.edit_employee, login_url="/login/")),
    path('delete_employee/', login_required(views.delete_employee.as_view()), name="delete_employee"),  # AJAX to Delete Order

    path('add-device/', login_required(views.add_device, login_url="/login/")),  # Add Device
    path('edit-device/<slug:id>', login_required(views.edit_device, login_url="/login/")),  # Edit Products
    path('deletedevice/', login_required(views.deletedevice.as_view()), name="deletedevice"),  # AJAX to Delete Product
    path('view-devices', login_required(views.view_devices, login_url="/login/")),  # View Products


    path('product-images/<slug:slug>', login_required(views.product_images, login_url="/login/")),
    path('del-product-image/<slug:slug>', login_required(views.del_product_image, login_url="/login/")),
    path('del-all-product-images/<slug:slug>', login_required(views.del_all_product_images, login_url="/login/")),

]
