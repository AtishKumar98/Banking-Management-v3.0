from http.client import HTTPResponse
from django.db import models
from django.contrib.auth.models import User
from django.db import transaction
from Account.models import *


# Create your models here.
class TransferMoney(models.Model):

    CREDIT = 'CREDIT'
    DEBIT = 'DEBIT'
    TRANSACTION_TYPES = (
        ("CREDIT", "Credit"),
        ("DEBIT", "Debit"),
    )
    # from_acc = models.ForeignKey(UserBankAccount, on_delete=models.CASCADE ,blank=False)
    # name = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    From_accno = models.ForeignKey(UserBankAccount, on_delete=models.CASCADE, related_name = 'From_accno')
    To_accno = models.ForeignKey(UserBankAccount, on_delete=models.CASCADE, related_name = 'To_accno')
    amount = models.CharField(max_length=50,blank=False)
    status = models.CharField(max_length=50,blank=False)
    Type = models.CharField(choices=TRANSACTION_TYPES, max_length=6,default ='DEBIT')
    # interset = models.CharField(max_length=50, null=True, blank=True)
    transaction_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)


    # @property
    # def calculate_interest(user_account):
    #     user_account = UserBankAccount.objects.all()
    #     for account in user_account:
    #         user_interest = (account.balance * (1 + (account.rate % account.period))) - account.balance
    #         account.save()
    #         return user_interest    
# with transaction.atomic():
#     @property

#     def get_transaction_balance(self):
#         user_account = UserBankAccount.objects.get(account_no = self.From_accno.account_no)
#         user_account_2 = UserBankAccount.objects.get(account_no = self.To_accno.account_no)
#         if self.Type == TransferMoney.DEBIT:
#             if user_account.balance <= 0:
#                 user_balance = user_account.balance - self.amount
#             else:
#                 HTTPResponse("insufficent Balance")
#         else:
#             user_balance = user_account.balance + self.amount
#         return user_balance


#     def save(self, *args, **kwargs):
#         # self.interest = self.calculate_interest
#         self.transaction_balance = self.get_transaction_balance
#         super(TransferMoney, self).save(*args, **kwargs)

    def __str__(self):
        return f" Type: {self.Type} |  From:{self.From_accno} |  To:{self.To_accno} |Amount ₹ {self.amount} | Balance After Transcation :{self.transaction_balance} | Status: {self.status}"