from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomerQueryForm

# Create your views here.


def customerquery(request):
   form = CustomerQueryForm
   if request.method=='POST':
      customerqueryform = CustomerQueryForm(request.POST)
      
      if customerqueryform.is_valid():
         customerqueryform.save()
         messages.success(request,'Your Customer Query Form has been submitted sucessfully.. Thank You!!!')
         return redirect('/customerquery')

   return render (request, 'CustomerQ.html',{'form':form})