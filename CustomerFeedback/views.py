from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomerFeedbackForm

# Create your views here.


def customerfeedback(request):
   form = CustomerFeedbackForm
   if request.method=='POST':
      customerfeedbackform = CustomerFeedbackForm(request.POST)
      
      if customerfeedbackform.is_valid():
         customerfeedbackform.save()
         messages.success(request,'Your Customer Feedback Form has been submitted sucessfully.. Thank You!!!')
         return redirect('/customerfeedback')

   return render (request, 'CustomerF.html',{'form':form})