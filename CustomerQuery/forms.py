from logging import PlaceHolder
from django import forms
from django.forms import ModelForm
from .models import CustomerQuery

class CustomerQueryForm(ModelForm):
    class Meta:
        model = CustomerQuery
        widgets = {
            'first_Name': forms.TextInput(attrs={'placeholder':'Please enter your First Name'}),
            'last_Name': forms.TextInput(attrs={'placeholder':'Please enter your Last Name'}),
            'email_Address': forms.TextInput(attrs={'placeholder':'Please enter your Email Address'}),
            'phone_Number': forms.TextInput(attrs={'placeholder':'Please enter your Phone Number'}),
            # 'query_Title': forms.TextInput(attrs={'placeholder':'Please enter your Full Name'}),
            'query_Description': forms.TextInput(attrs={'placeholder':'Please enter Query Description'})
        }
        fields = '__all__'