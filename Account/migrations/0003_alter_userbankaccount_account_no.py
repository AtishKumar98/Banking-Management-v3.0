# Generated by Django 4.0.4 on 2022-06-05 13:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_alter_userbankaccount_account_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbankaccount',
            name='account_no',
            field=models.BigIntegerField(blank=True, unique=True, validators=[django.core.validators.MinValueValidator(1000000000000000000), django.core.validators.MaxValueValidator(999000000000)]),
        ),
    ]
