from django.db import models
from Customer.models import Customer
from Product.models import *
import random
from django.contrib.auth.models import User
from .utils import *
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)

import string
from django.db.models  import Max
# Create your models here.
MALE = 'M'
FEMALE = 'F'


GENDER_CHOICE = (
    (MALE, "Male"),
    (FEMALE, "Female"),
)
class UserBankAccount(models.Model):
    Account_id = models.AutoField(primary_key=True,editable=False,unique=True)
    user = models.ForeignKey(
        User,   
        related_name='account',
        on_delete=models.CASCADE,
    )
    account_type = models.ForeignKey(
        ProductCode,
        default=1,
        related_name='accounts',
        on_delete=models.CASCADE
    )
    period = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    rate = models.DecimalField(max_digits=4, decimal_places=2, default=0) 
    account_no = models.PositiveBigIntegerField(null=False,blank=True,unique=True)
    account_no = models.BigIntegerField(null=False,blank=True,unique=True)
    balance = models.DecimalField(
       max_digits=6, decimal_places=2, default=0, null=True, blank=True
    )
    interest_start_date = models.DateField(
        auto_now_add=True,
        help_text=(
            'The month number that interest calculation will start from'
        )
    )
    initial_deposit_date = models.DateField(auto_now_add=True)

    Referrence_Number = models.CharField(max_length = 10,
           blank=True,
           editable=False,
           unique=True,
           default=create_new_ref_number,
      )


    def create_new_ref_number():
                not_unique = True
                while not_unique:
                    unique_ref = random.randint(1000000000, 9999999999)
                    if not UserBankAccount.objects.filter(Referrence_Number=unique_ref):
                        not_unique = False
                return str(unique_ref)

    def save(self,*args, **kwargs):
        # if self.account_tid == "":
        #     self.account_tid = generate_code()
        # self.full_no = int(1001) if UserBankAccount.objects.count() == 0 else UserBankAccount.objects.aggregate(max=Max[int(self.full_no)])["max"]+1
        # self.full_no =''.join(random.choices(string.digits, k=3))
        self.account_no = f"{self.account_type.code}0000{self.user.id}{self.Referrence_Number}"
        # .join(random.choices(string.digits, k=4))
        return super(UserBankAccount, self).save(*args,**kwargs)

    def __str__(self):
        return str(self.account_no)

    