from http.client import HTTPResponse
from django.shortcuts import render
from .models import *
from Transfer.models import*
from .forms import *
# Create your views here.
def index(request):
    current_user = request.user.customer
    current_user_file = UserBankAccount.objects.filter(user = request.user)
    # bing = list(current_user_file.keys())
    # print(bing)

    # form = AccountForm ()
    form = AccountForm(instance=current_user)
    # acc_no = 1001 if UserBankAccount.objects.count() == 0 else UserBankAccount.objects.aggregate(max=Max['full_no'])["max"]+1
    if request.method=='POST':
        current_user = request.POST.get('username')
        form = AccountForm(request.POST)
        if form.is_valid():
            

            # username = form.cleaned_data['user']
            Account_type = form.cleaned_data['account_type']
            period = form.cleaned_data['period']
            rate = form.cleaned_data['rate']
            balance = form.cleaned_data['balance']
            data = UserBankAccount.objects.create(
                user = current_user,
                account_type=Account_type,
                period=period,
                rate=rate,
                balance=balance
                )
            data.save()
            form.save()
        else:
           return  HTTPResponse('Invalid Data')
    context = { 'form':form,'all_acc':current_user_file}
    return render(request, 'account.html', context)

    
def report(request,pk):
  current_user_file = UserBankAccount.objects.filter(user = request.user)
  transfer_report = UserBankAccount.objects.get(Account_id=pk)
  transfer_report2 = TransferMoney.objects.filter(From_accno=transfer_report)
  transfer_report3 = TransferMoney.objects.filter(To_accno=transfer_report)
  print(transfer_report3)
  # transfer_report = TransferMoney.objects.get()
  transfer_report1 = request.user.account.all()
  context= {
    'report2':transfer_report,
    'b':transfer_report2,
    'c':transfer_report3,
    }
  return render (request, 'report.html',context)