from faulthandler import disable
from django import forms

class Payment(forms.Form):
  payor = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your Account', }) , max_length=30)
  payee = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'To Account'}) , max_length=30)
  amount = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Amount in ₹'}) , max_length=30)