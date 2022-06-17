from django.shortcuts import render, redirect

# Create your views here.

def tnc(request):
    return render (request, 'TNC.html')