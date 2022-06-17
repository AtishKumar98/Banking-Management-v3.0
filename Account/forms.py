from django import forms
from django.forms import ModelForm, fields
from .models import *



class AccountForm(ModelForm):
    class Meta:
        model = UserBankAccount
        fields = '__all__'
        exclude = ['account_no',]