from django.contrib import admin

# Register your models here.
from .models import *


# admin.site.register(Services)

@admin.register(Services)
class services(admin.ModelAdmin):
    list_display = ['full_Name','account_No','services_Types','amount','email_ID']
    search_fields = ['full_Name','account_No','email_ID']
    list_filter = ('services_Types', 'amount')



