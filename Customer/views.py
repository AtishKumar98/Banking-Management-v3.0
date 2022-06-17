from django.shortcuts import render, redirect

from Customer.models import Customer
from .forms import CustomerForm
# Create your views here.



# def Customer_Detail(request):





def Customer_Update(request):
    # cust_update = Customer.objects.get(id )
    cust_user = request.user.customer
    form = CustomerForm(instance = cust_user)
    if request.method == "POST":
        # print("print POST",request.POST)
        form = CustomerForm(request.POST,instance = cust_user)
        if form.is_valid() :
            form.save()
            return redirect ('/')
    context = {'form':form,}
    return render(request, 'customer.html',context)
from django.shortcuts import render

# Create your views here.
