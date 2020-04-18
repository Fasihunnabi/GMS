from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


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


class user_update_form(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1')

    def __init__(self, *args, **kwargs):
        super(user_update_form, self).__init__(*args, **kwargs)
        # self.fields['no_of_stores'].widget.attrs['required'] = True
        self.fields['username'].widget.attrs['placeholder'] = "User Name"
        self.fields['username'].widget.attrs['class'] = 'form-control'

        self.fields['email'].widget.attrs['placeholder'] = "Email"
        self.fields['email'].widget.attrs['class'] = 'form-control'

        self.fields['password1'].required = False
        self.fields['password2'].required = False




class user_register_form(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(user_register_form, self).__init__(*args, **kwargs)
        # self.fields['no_of_stores'].widget.attrs['required'] = True
        self.fields['username'].widget.attrs['placeholder'] = "User Name"
        self.fields['username'].widget.attrs['class'] = 'form-control'

        self.fields['email'].widget.attrs['placeholder'] = "Email"
        self.fields['email'].widget.attrs['class'] = 'form-control'

        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].widget.attrs['class'] = 'form-control'

        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'



class Employee_form(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['device_id', 'dateOfBirth', 'phone', 'address', 'cnic', 'designation', 'emp_delete', 'emp_type']
        exclude = ['emp_User', 'emp_supervisor']

    def __init__(self, supervisor, *args, **kwargs):
        super(Employee_form, self).__init__(*args, **kwargs)

        self.fields['dateOfBirth'].widget.attrs['placeholder'] = "Date of Birth ()"
        self.fields['dateOfBirth'].widget.attrs['class'] = 'form-control'

        self.fields['phone'].widget.attrs['placeholder'] = 'Phone'
        self.fields['phone'].widget.attrs['class'] = 'form-control'

        self.fields['address'].widget.attrs['placeholder'] = 'Address'
        self.fields['address'].widget.attrs['class'] = 'form-control'

        self.fields['cnic'].widget.attrs['placeholder'] = 'CNIC'
        self.fields['cnic'].widget.attrs['class'] = 'form-control'

        self.fields['designation'].widget.attrs['placeholder'] = 'Designation'
        self.fields['designation'].widget.attrs['class'] = 'form-control'

        self.fields['emp_type'].empty_label = '--- Employee Type ---'
        self.fields['emp_type'].widget.attrs['class'] = 'form-control'


        self.fields['device_id'] = forms.ModelChoiceField(
            required=True, queryset=Device.objects.filter(Engine_supervisor=supervisor),
            empty_label='--- Select Power Generator ---'
        )

        self.fields['device_id'].widget.attrs['class'] = 'form-control'
