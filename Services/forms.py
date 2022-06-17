from logging import PlaceHolder
from django import forms
from django.forms import ModelForm
from .models import Services

class ServicesForm(ModelForm):
    class Meta:
        model = Services
        widgets = {
            'full_Name': forms.TextInput(attrs={'placeholder':'Please enter your Full Name'}),
            'account_No': forms.TextInput(attrs={'placeholder':'Please enter your Account Number'}),
            # 'services_types': forms.TextInput(attrs={'placeholder':'Please select Service Type'}),
            # 'amount': forms.TextInput(attrs={'placeholder':'Please select specific Amount'}),
            # 'email_ID': forms.TextInput(attrs={'placeholder':'Please enter your Email Address'}),
            'mobile_No': forms.TextInput(attrs={'placeholder':'Please enter your Mobile Number'}),
            'address': forms.TextInput(attrs={'placeholder':'Please enter your complete Address'}),
        }
        fields = '__all__'