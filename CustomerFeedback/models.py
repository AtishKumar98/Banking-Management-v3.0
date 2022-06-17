from typing_extensions import Required
from django import forms
from django.db import models

class CustomerFeedback(models.Model):

    comment_titles = [
        ("Compliment","Compliment"),
        ("Complaint","Complaint")        
    ]

    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone_No = models.CharField(max_length=10)
    comment_Title = models.CharField(choices=comment_titles, max_length=30)
    comments = models.TextField(max_length=500)


    def __str__(self):
        return self.name
    