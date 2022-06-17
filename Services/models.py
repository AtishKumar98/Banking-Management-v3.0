from typing_extensions import Required
from django import forms
from django.db import models

class Services(models.Model):
    
    service_types = [
        ("Cash Pickup","Cash Pickup"),
        ("Cash Delivery","Cash Delivery")        
    ]

    amount_choices = [
        ("5000","5000"),
        ("10000","10000"),
        ("15000","15000"),
        ("20000","20000"),        
    ]

    full_Name = models.CharField(max_length=30)
    account_No = models.CharField(max_length=10)
    services_Types = models.CharField(choices=service_types, max_length=30)    
    amount = models.CharField(choices=amount_choices, max_length=30, default=5000)
    email_ID = models.EmailField(max_length=20)
    mobile_No = models.CharField(max_length=10)
    address = models.TextField(max_length=200)
    i_Agree_to_the_Terms_and_Conditions = models.BooleanField(default=True)
   

    def __str__(self):
        return self.account_No  