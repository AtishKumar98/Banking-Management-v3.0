from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ServicesForm

# Create your views here.


def services(request):
   form = ServicesForm
   if request.method=='POST':
      servicesform = ServicesForm(request.POST)
      
      if servicesform.is_valid():
         servicesform.save()
         messages.success(request,'Your Doorstep Banking Service Request has been submitted sucessfully.. Thank You!!!')
         return redirect('/services')

   return render (request, 'DoorstepB.html',{'form':form})