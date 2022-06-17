from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(CustomerFeedback)
class CustomerFeedbacK(admin.ModelAdmin):
    search_fields = ['name','email','phone_No']
    list_display = ['name','email','phone_No','comment_Title']
    