from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['sku'].widget.attrs['class'] = 'form-control'
        self.fields['sku'].widget.attrs['placeholder'] = 'Enter Article Number'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Enter the Name of the Product'
        self.fields['sale_price'].widget.attrs['class'] = 'form-control'
        self.fields['sale_price'].widget.attrs['placeholder'] = 'Enter Sale Price'
        self.fields['original_price'].widget.attrs['class'] = 'form-control'
        self.fields['original_price'].widget.attrs['placeholder'] = 'Enter Original Price'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['placeholder'] = 'Enter the Short Description of the Product'
        self.fields['description'].widget.attrs['rows'] = 5
        self.fields['category'].widget.attrs['class'] = 'form-control custom-select'


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

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name',
                  'owned_by',
                  'Engine_Brand',
                  'Engine_Displacement',
                  'Engine_Maximum_Output',
                  'Engine_Type',
                  'Engine_Oil_Alert_System',
                  'Engine_Ignition_System',
                  'Engine_Start',
                  'Generator_Alternator',
                  'Voltage_Regulator',
                  'Phase',
                  'ACMax_Output',
                  'AC_Rated_Output',
                  'Rated_Voltage',
                  'DC_Output',
                  'Rated_Power_Factor',
                  'Pilot_Lamp',
                  'Volt_Meter',
                  'Fuel_Tank_Capacity',
                  'Continuous_Operating_Hours',
                  'Dimensions_L_W_H',
                  'Dry_Weight'
                  ]
        exclude = ['Engine_supervisor']

    def __init__(self, *args, **kwargs):
        super(DeviceForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['owned_by'].widget.attrs['class'] = 'form-control'
        self.fields['Engine_Brand'].widget.attrs['class'] = 'form-control'
        self.fields['Engine_Displacement'].widget.attrs['class'] = 'form-control'
        self.fields['Engine_Maximum_Output'].widget.attrs['class'] = 'form-control'
        self.fields['Engine_Type'].widget.attrs['class'] = 'form-control'
        self.fields['Engine_Oil_Alert_System'].widget.attrs['class'] = 'form-control'
        self.fields['Engine_Ignition_System'].widget.attrs['class'] = 'form-control'
        self.fields['Engine_Start'].widget.attrs['class'] = 'form-control'
        self.fields['Generator_Alternator'].widget.attrs['class'] = 'form-control'
        self.fields['Voltage_Regulator'].widget.attrs['class'] = 'form-control'
        self.fields['Phase'].widget.attrs['class'] = 'form-control'
        self.fields['ACMax_Output'].widget.attrs['class'] = 'form-control'
        self.fields['AC_Rated_Output'].widget.attrs['class'] = 'form-control'
        self.fields['Rated_Voltage'].widget.attrs['class'] = 'form-control'
        self.fields['DC_Output'].widget.attrs['class'] = 'form-control'
        self.fields['Rated_Power_Factor'].widget.attrs['class'] = 'form-control'
        self.fields['Pilot_Lamp'].widget.attrs['class'] = 'form-control'
        self.fields['Volt_Meter'].widget.attrs['class'] = 'form-control'
        self.fields['Fuel_Tank_Capacity'].widget.attrs['class'] = 'form-control'
        self.fields['Continuous_Operating_Hours'].widget.attrs['class'] = 'form-control'
        self.fields['Dimensions_L_W_H'].widget.attrs['class'] = 'form-control'
        self.fields['Dry_Weight'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Device Name'
        self.fields['owned_by'].widget.attrs['placeholder'] = 'Owned By'
        self.fields['Engine_Brand'].widget.attrs['placeholder'] = 'e.g: Honda'
        self.fields['Engine_Displacement'].widget.attrs['placeholder'] = 'e.g: 389 cc (cm)'
        self.fields['Engine_Maximum_Output'].widget.attrs['placeholder'] = 'e.g: 9.6kW / 13.0HP'
        self.fields['Engine_Type'].widget.attrs['placeholder'] = 'e.g: Air Cooled, 4-cycle, OHV Gasoline Engine'
        self.fields['Engine_Oil_Alert_System'].widget.attrs['placeholder'] = 'e.g: Standard'
        self.fields['Engine_Ignition_System'].widget.attrs['placeholder'] = 'e.g: Transistor (C.D.I.)'
        self.fields['Engine_Start'].widget.attrs['placeholder'] = 'e.g: Electric Start'
        self.fields['Generator_Alternator'].widget.attrs['placeholder'] = 'e.g: Self-Exciting, 2-Pole, Field Rotating Type, Single Phase'
        self.fields['Voltage_Regulator'].widget.attrs['placeholder'] = 'e.g: AVR'
        self.fields['Phase'].widget.attrs['placeholder'] = 'e.g: single'
        self.fields['ACMax_Output'].widget.attrs['placeholder'] = 'e.g: 5.5kVA / 50Hz'
        self.fields['AC_Rated_Output'].widget.attrs['placeholder'] = 'e.g: 5.0kVA / 50Hz'
        self.fields['Rated_Voltage'].widget.attrs['placeholder'] = 'e.g: 220V / 50Hz'
        self.fields['DC_Output'].widget.attrs['placeholder'] = 'e.g: 12V-8.3A (Receptacle)'
        self.fields['Rated_Power_Factor'].widget.attrs['placeholder'] = 'e.g: 1 cos'
        self.fields['Pilot_Lamp'].widget.attrs['placeholder'] = 'e.g: Standard'
        self.fields['Volt_Meter'].widget.attrs['placeholder'] = 'e.g: Standard'
        self.fields['Fuel_Tank_Capacity'].widget.attrs['placeholder'] = 'e.g: 25 Liters'
        self.fields['Continuous_Operating_Hours'].widget.attrs['placeholder'] = 'e.g: 9.0 Hours (100% Load)'
        self.fields['Dimensions_L_W_H'].widget.attrs['placeholder'] = 'e.g: 685mm x 534mm x 509mm'
        self.fields['Dry_Weight'].widget.attrs['placeholder'] = 'e.g: 85 kg'
