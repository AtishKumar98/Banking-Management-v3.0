from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(UserBankAccount)


@admin.register(UserBankAccount)
class BankAdmin(admin.ModelAdmin):
    search_fields = ['user','account','account_type','balance',]
    list_display = ['user','account_no','account_type','balance',]

