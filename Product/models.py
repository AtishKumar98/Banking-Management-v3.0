from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)
from decimal import Decimal
# Create your models here.

class ProductCode(models.Model):
    code = models.CharField(max_length=6, default=0,help_text='Enter Product Code',unique=True)
    name = models.CharField(max_length=128,help_text='Enter Product Code eg:Saving/Fixed Deposit')
    maximum_withdrawal_amount = models.DecimalField(
        decimal_places=2,
        max_digits=12
    )
    annual_interest_rate = models.DecimalField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        decimal_places=2,
        max_digits=5,
        help_text='Interest rate from 0 - 100'
    )
    interest_calculation_per_year = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(12)],
        help_text='The number of times interest will be calculated per year'
    )

    def __str__(self):
        return self.name

    # def calculate_interest(self, principal):
    #     """
    #     Calculate interest for each account type.

    #     This uses a basic interest calculation formula
    #     """
    #     p = principal
    #     r = self.annual_interest_rate
    #     n = Decimal(self.interest_calculation_per_year)

    #     # Basic Future Value formula to calculate interest
    #     interest = (p * (1 + ((r/100) / n))) - p

    #     return round(interest, 2)