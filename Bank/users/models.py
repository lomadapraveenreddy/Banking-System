from django.db import models
from django.contrib.auth.models import User
import random,string
# Create your models here.

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    amount=models.BigIntegerField(default=3000)
    accountNumber=models.CharField(max_length=10,default='0123456789')#101
    def __str__(self):
        return f'{self.user.username} customer'


class Transaction(models.Model):
    transactionID=models.CharField(max_length=15,unique=True)
    dateTime=models.DateTimeField(auto_now=True)
    transactionAmount=models.BigIntegerField()
    loan=models.BooleanField(default=False)
    transactionFrom=models.ForeignKey(User,on_delete=models.CASCADE,related_name='debited')
    transactionTo=models.ForeignKey(User,on_delete=models.CASCADE,related_name='credited',default=None)
    success=models.BooleanField(default=False)

    def __str__(self):
        return f'{self.transactionID} transaction from {self.transactionFrom.username} to {self.transactionTo.username}'
    
class Complaint(models.Model):
    complaintID=models.CharField(max_length=15,unique=True)
    complaintUser=models.ForeignKey(User,on_delete=models.CASCADE)
    transaction=models.ForeignKey(Transaction,on_delete=models.CASCADE)
    dateTime=models.DateTimeField(auto_now=True)
    text=models.TextField(max_length=180)
    status=models.BooleanField(default=False)


    def __str__(self):
        return f' complaint {self.complaintID} of {self.transaction}'

class Loan(models.Model):
    loanID=models.CharField(max_length=15,unique=True)
    loanUser=models.ForeignKey(User,on_delete=models.CASCADE)
    dateTime=models.DateTimeField(auto_now=True)
    loanAmount=models.BigIntegerField()
    loanAbout=models.TextField()

    def __str__(self):

        return f'loan to {self.loanUser.username} of {self.loanAmount}'



class DebitCard(models.Model):
    cardUser=models.ForeignKey(User,on_delete=models.CASCADE)
    cardNumber=models.CharField(max_length=12)
    nameOnCard=models.CharField(max_length=18)
    expiryDate=models.DateTimeField(auto_now=True)
    cvv=models.PositiveIntegerField()
    pin=models.PositiveIntegerField()

    def __str__(self):
        return f'Debit Card of {self.cardUser.username}'