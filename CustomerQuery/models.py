from typing_extensions import Required
from django import forms
from django.db import models

class CustomerQuery(models.Model):
    
    query_types = [
        ("Registration Process","Registration Process"),
        ("Dashboard","Dashboard"),
        ("Account","Account"),
        ("Transfer","Transfer"),
        ("My Profile","My Profile"),
        ("Banking Services","Banking Services"),
        ("Customer Feedback Form","Customer Feedback Form"), 
        ("Customer Query Form","Customer Query Form"),    
        ("Contact Us","Contact Us")
     ]
    
    first_Name = models.CharField(max_length=30)
    last_Name = models.CharField(max_length=30)
    email_Address = models.EmailField(max_length=30)
    phone_Number = models.CharField(max_length=10)
    query_Title = models.CharField(choices=query_types, max_length=30)
    query_Description = models.TextField(max_length=500)
   

    def __str__(self):
        return self.query_Title    