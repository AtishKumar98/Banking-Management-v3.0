from django.contrib import admin

from CustomerQuery.forms import CustomerQueryForm
from .models import *

# Register your models here.


@admin.register(CustomerQuery)
class CustomerQuery(admin.ModelAdmin):
    search_fields = ['first_Name','email_Address','phone_Number']
    list_display = ['first_Name','last_Name','email_Address','phone_Number','query_Title']

