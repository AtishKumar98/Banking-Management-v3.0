from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', index,name='home' ),
    path('login/' , loginpage, name = 'loginpage'),
    path('logout/', logoutUser, name='logout'),
    path('dashboard/', Dashboard, name='dashboard'),
    path('update/<str:pk>/', update_cust, name='update'),
    path('delete_cust/<str:pk>/', delete_cust,name='delete_cust'),
    path('delete_acc/<str:pk>/', delete_account,name='delete_acc'),
]
