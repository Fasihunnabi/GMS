from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(required=True, error_messages={'required': 'Please enter the password'}, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))