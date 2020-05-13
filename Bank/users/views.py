from django.views.generic import (
    DetailView,
    ListView,
)
from .models import Customer
from django.shortcuts import render,reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User 
from .forms import NewTransactionForm
from .models import Transaction,Customer
from django.contrib import messages
import time,string,random
# Create your views here.
@login_required
def home(request):
    customerObj=request.user.customer
    return render(request,'users/home.html',{'balance':customerObj.amount})

def about(request):
    return render(request,'users/about.html')

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
                messages.warning(request,f'Transaction failed:Insufficient Funds')
            txnobject=Transaction(transactionID=''.join(random.choices(string.ascii_letters + string.digits, k=15)),transactionAmount=amount,transactionFrom=sender,transactionTo=User.objects.filter(username=username).first(),success=success)
            txnobject.save()
            if(success):
                return HttpResponseRedirect(reverse('users:home'))
            else:
                return HttpResponseRedirect(reverse('users:new-transaction'))
    else:
        form=NewTransactionForm()

    return render(request,'users/new_transaction.html',{'form':form})

# @login_required
# def myTransactions(request):
#     transactions=list(request.user.debited.all())+list(request.user.credited.all())
#     return render(request,'users/my_transactions.html',{'transactions':transactions})

class TransactionListView(ListView):
    model=Transaction
    context_object_name='transactions'
    ordering=['-dateTime']
    
    def get_queryset(self):
        queryset=super().get_queryset()
        transactions=list(queryset.filter(transactionFrom=self.request.user))
        transactions+=list(queryset.filter(transactionTo=self.request.user))
        return transactions


class ProfileDetailView(DetailView):
    model=Customer

    def get_object(self,**kwargs):
        user=None    
        user=User.objects.filter(username=self.kwargs['username']).first()
        return get_object_or_404(Customer,user=user)

class TransactionDetailView(DetailView):
    model=Transaction
    context_object_name='transaction'
    def get_object(self,**kwargs):
        return get_object_or_404(Transaction,transactionID=self.kwargs['transactionID'])