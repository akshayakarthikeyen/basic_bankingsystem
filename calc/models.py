from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    balance = models.IntegerField()
    accountnumber = models.IntegerField()

class transactionhistory(models.Model):
    source_name = models.CharField(max_length=100)
    source_email = models.EmailField(max_length=100)
    available_balance = models.IntegerField()
    transfered_amount = models.IntegerField()
    source_accountnumber = models.IntegerField()
    destination_name = models.CharField(max_length=122)
    date = models.DateField()
