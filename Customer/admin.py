from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Customer)
class Customer(admin.ModelAdmin):
    list_display = ['First_Name', 'PAN','Aadhar', ]
    search_fields = ['First_Name', 'PAN','Aadhar', ]




# admin.site.register(CustomerAdmin)
