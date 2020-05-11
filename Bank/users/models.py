from django.db import models
from django.contrib.auth.models import User
import random,string
# Create your models here.

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    amount=models.BigIntegerField(default=3000)

    def __str__(self):
        return f'{self.user.username} customer'


class Transaction(models.Model):
    transactionID=models.CharField(max_length=15,unique=True,default=''.join(random.choices(string.ascii_letters + string.digits, k=15)))
    dateTime=models.DateTimeField(auto_now=True)
    transactionAmount=models.BigIntegerField()
    transactionFrom=models.ForeignKey(User,on_delete=models.CASCADE,related_name='debited')
    transactionTo=models.ForeignKey(User,on_delete=models.CASCADE,related_name='credited',default=None)
    success=models.BooleanField(default=False)

    def __str__(self):
        return f'{self.transactionFrom.username} transaction'
    
