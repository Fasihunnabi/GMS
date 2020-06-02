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

    path('signup', views.user_creation ),  #After Login yahan redirect krna
    path('', login_required(views.index, login_url="/login/")),  #After Login yahan redirect krna
    path('index/<slug:device_id>', login_required(views.index_with_id, login_url="/login/")),  #After Login yahan redirect krna

    path('employee', login_required(views.view_employee, login_url="/login/")),  # View Orders
    path('add-employee/', login_required(views.add_employee, login_url="/login/")),
    path('edit-employee/<slug:id>', login_required(views.edit_employee, login_url="/login/")),
    path('delete_employee/', login_required(views.delete_employee.as_view()), name="delete_employee"),  # AJAX to Delete Order

    path('add-device/', login_required(views.add_device, login_url="/login/")),  # Add Device
    path('edit-device/<slug:id>', login_required(views.edit_device, login_url="/login/")),  # Edit Products
    path('deletedevice/', login_required(views.deletedevice.as_view()), name="deletedevice"),  # AJAX to Delete Product
    path('view-devices', login_required(views.view_devices, login_url="/login/")),  # View Products

    path('add-sensor/', login_required(views.add_sensor, login_url="/login/")),  # Add Device
    path('edit-sensor/<slug:id>', login_required(views.edit_sensor, login_url="/login/")),  # Edit Products
    path('deletesensor/', login_required(views.deletesensor.as_view()), name="deletesensor"),  # AJAX to Delete Product
    path('view-sensor', login_required(views.view_sensor, login_url="/login/")),  # View Products

    path('view-cases', login_required(views.view_cases, login_url="/login/")),  # View Products
    path('add-case', login_required(views.add_case, login_url="/login/")),  # Edit Products
    path('deletecase/', login_required(views.deletecase.as_view()), name="deletecase"),  # AJAX to Delete Product
    path('edit-case/<slug:id>', login_required(views.edit_case, login_url="/login/")),  # Edit Products

    path('sensor_reading/', login_required(views.sensor_reading.as_view()), name="sensor_reading"),  # AJAX to Delete Product

    path('case_exist/', login_required(views.case_exist.as_view()), name="case_exist"),  # AJAX to Delete Product



]
