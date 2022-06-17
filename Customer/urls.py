from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    # path('', Customer_Detail, name='customer_home' ),
    path('', Customer_Update, name='customer_update' ),
]
