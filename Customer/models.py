from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django_countries.data import COUNTRIES

from django.contrib.auth.models import AbstractUser
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)

# Create your models here.

Customer_Prefix = (
        ('Mr' , "MR"),
        ('Ms' , "MS"),
        ('Mrs' , "MRS"),
    )
Type =(
        ('1' , "Individual"),
        ('2' , "Other"),
        
    )

Other_Prefix = (
        ('1' , "Charity"),
        ('2' , "Company"),
        ('3' , "Organisation"),
    )
state_choices = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))
GENDER = (
    ('1','Male'),
    ('2','Female'),
)

class Customer(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE,null=True) 
    # Customer_Type = models.CharField(max_length=25, choices = Type, default='1')
    Name_title = models.CharField(max_length=25, choices = Customer_Prefix) 
    First_Name = models.CharField(max_length=25)
    Middle_Name = models.CharField(max_length=25)
    Last_Name = models.CharField(max_length=25)
    Gender  = models.CharField(max_length=25, choices = GENDER, default='1')
    Father_Name = models.CharField(max_length=25)
    Mother_Name = models.CharField(max_length=25)
    Date_of_Birth = models.DateField(null=True)
    Aadhar = models.BigIntegerField(default=0, validators=[MinValueValidator(200000000000), MaxValueValidator(999000000000)]
    )
    PAN = models.CharField(max_length=10)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    District = models.CharField(max_length=25,default='Raigad')
    state = models.CharField(
        "State",
        max_length=1024,
        choices = state_choices,
        default="Maharashtra"
    )
    country = models.CharField(
        "Country",
        max_length=2,
        choices=sorted(COUNTRIES.items()),
        default="IN"
    )
    zip = models.CharField(max_length=100)
    # address_type = models.CharField(max_length=1)
    def __str__(self):
        return self.First_Name
