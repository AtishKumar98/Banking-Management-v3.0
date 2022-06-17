from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .form import *
from Account.models import *
from Customer.models import *
from Customer.forms import *

from django.contrib.auth.decorators import login_required
from django.contrib import messages



@login_required(login_url='/login/')
def logoutUser(request):
    logout(request)
    return redirect('/login/')





def loginpage(request):
    if request.method == "POST" and 'form1' in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session.set_expiry(5000)
            return redirect('/')
        else:
            messages.error(request, 'INCORRECT USERNAME OR PASSWORD! TRY AGAIN')
    

    form = CreateUserForm()
    if request.method == 'POST' and 'form2' in request.POST:
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account Created Successfully for ' + username)

    context = {'form': form }

    return render(request, 'login.html', context)

# @login_required(login_url='/login/')
def index(request):
    context= {}
    return render (request, 'home.html' , context)

def Dashboard(request):
    all_account = UserBankAccount.objects.all()
    all_customer = Customer.objects.all()
    context = {
        'account':all_account,
        'customer':all_customer, 
  
    }
    return render (request, 'dashboard.html', context)


def update_cust(request,pk):
    cust_update = Customer.objects.get(id=pk)
    form_update = CustomerForm(instance=cust_update)
    if request.method =="POST":
        form_update = CustomerForm(request.POST, instance=cust_update)
        if form_update.is_valid():
            form_update.save()
            messages.success(request , "Customer Updated Succesfully")
            return redirect ('/')
    context = { 'form_update':form_update}
    return render (request, 'update_cust.html', context)




def delete_cust(request,pk):
    cust_delete = Customer.objects.get(id=pk)
    if request.method=="POST":
        cust_delete.delete()
        messages.error(request , "Customer Deleted Succesfully")
        return redirect('/')
    context = {'cust_delete':cust_delete}
    return render(request, 'delete.html',context)



def delete_account(request,pk):
    cust_delete = UserBankAccount.objects.get(Account_id=pk)
    if request.method=="POST":
        cust_delete.delete()
        messages.error(request , "Account Deleted Succesfully")
        return redirect('/')
    context = {'cust_delete':cust_delete}
    return render(request, 'delete.html',context)
    return render (request, 'home.html' , context)
