from django.shortcuts import render,reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User 
from .forms import NewTransactionForm
from .models import Transaction,Customer
from django.contrib import messages
import time
# Create your views here.
@login_required
def home(request):
    customerObj=request.user.customer
    return render(request,'users/home.html',{'balance':customerObj.amount})

@login_required
def newTransaction(request):
    if request.method=='POST':
        form=NewTransactionForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            print(username)
            amount=form.cleaned_data.get('amount')
            sender=request.user
            if sender.customer.amount>=amount:
                print('amount')
                if User.objects.filter(username=username):
                    print('filter')
                    sender.customer.amount-=amount
                    receiver=User.objects.filter(username=username).first()
                    receiver.customer.amount+=amount
                    sender.customer.save()
                    receiver.customer.save()
                    success=True
                    messages.success(request,f'Sucessfully transferred to {username}')
                else:
                    messages.warning(request,f'No user exists')
                    return HttpResponseRedirect(reverse('users:new-transaction'))
            else:
                success=False
                messages.warning(request,f'Insufficient Funds')
            txnObject=Transaction(transactionAmount=amount,transactionFrom=sender,transactionTo=User.objects.filter(username=username).first(), success=success)
            txnObject.save()
            if(success):
                return HttpResponseRedirect(reverse('users:home'))
            else:
                return HttpResponseRedirect(reverse('users:new-transaction'))
    else:
        form=NewTransactionForm()

    return render(request,'users/new_transaction.html',{'form':form})

@login_required
def myTransactions(request):
    transactions=request.user.debited.all()
    transactions= transactions or request.user.credited.all()
    return render(request,'users/my_transactions.html',{'transactions':transactions})
