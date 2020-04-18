from django import forms
from .models import Order, OrderDetail

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'customer_email', 'customer_phone', 'shipping_address']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['customer_name'].widget.attrs['class'] = 'form-control'
        self.fields['customer_name'].widget.attrs['placeholder'] = 'Enter your Full Name'
        self.fields['customer_name'].widget.attrs['autocomplete'] = "nope"
        self.fields['customer_email'].widget.attrs['class'] = 'form-control'
        self.fields['customer_email'].widget.attrs['placeholder'] = 'Enter your Email '
        self.fields['customer_email'].widget.attrs['autocomplete'] = "nope"
        self.fields['customer_phone'].widget.attrs['class'] = 'form-control'
        self.fields['customer_phone'].widget.attrs['placeholder'] = 'Enter your Cell #'
        self.fields['customer_phone'].widget.attrs['autocomplete'] = "nope"
        self.fields['shipping_address'].widget.attrs['class'] = 'form-control'
        self.fields['shipping_address'].widget.attrs['placeholder'] = 'Enter the Shipping Address'
        self.fields['shipping_address'].widget.attrs['autocomplete'] = "nope"


    # def __init__(self, *args, **kwargs):
    #     super(CustomerForm, self).__init__(*args, **kwargs)
    #     self.fields['cust_name'].widget.attrs['class'] = 'form-control'
    #     self.fields['cust_name'].widget.attrs['placeholder'] = 'Guest Name'
    #     self.fields['country'].widget.attrs['class'] = 'form-control'
    #     self.fields['country'].widget.attrs['placeholder'] = 'Country'
    #     self.fields['state'].widget.attrs['class'] = 'form-control'
    #     self.fields['state'].widget.attrs['placeholder'] = 'State'
    #     self.fields['city'].widget.attrs['class'] = 'form-control'
    #     self.fields['city'].widget.attrs['placeholder'] = 'City'
    #     self.fields['zip'].widget.attrs['class'] = 'form-control'
    #     self.fields['zip'].widget.attrs['placeholder'] = 'Zip Code'
    #     self.fields['email'].widget.attrs['class'] = 'form-control'
    #     self.fields['email'].widget.attrs['placeholder'] = 'Email Address'
    #     self.fields['phone'].widget.attrs['class'] = 'form-control'
    #     self.fields['phone'].widget.attrs['placeholder'] = 'phone Number'
    #     self.fields['address1'].widget.attrs['class'] = 'form-control guest-textarea'
    #     self.fields['address1'].widget.attrs['placeholder'] = 'Address1'
    #     self.fields['address1'].widget.attrs['rows'] = '1'
    #     self.fields['address2'].widget.attrs['class'] = 'form-control guest-textarea'
    #     self.fields['address2'].widget.attrs['placeholder'] = 'Address2'
    #     self.fields['address2'].widget.attrs['rows'] = '1'
    #     self.fields['additional_comments'].widget.attrs['class'] = 'form-control'
    #     self.fields['additional_comments'].widget.attrs['placeholder'] = 'Additional Comments'
    #     self.fields['additional_comments'].widget.attrs['rows'] = '3'
    #     self.fields['reward_type'].widget.attrs['class'] = 'form-control'
    #     self.fields['reward_points'].widget.attrs['class'] = 'form-control'
    #     self.fields['reward_points'].widget.attrs['placeholder'] = 'Reward Points'