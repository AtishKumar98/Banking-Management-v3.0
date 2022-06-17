from http.client import HTTPResponse
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
# from .models import *
from Transfer.models import*
# # Create your views here.




def index(request):
   return render (request, 'ContactUs.html')