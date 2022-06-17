from django import forms
from django.forms import ModelForm, fields
from .models import *



class CustomerForm(ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
        exclude = ['user']