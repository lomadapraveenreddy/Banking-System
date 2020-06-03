from django.views.generic import (
    DetailView,
    ListView,
    UpdateView,
    CreateView,
)
from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .forms import (NewTransactionForm,
                    UserUpdateForm, 
                    ComplaintCreationForm,
                    ApplyLoanForm,
                    )
from .models import Transaction, Customer, Complaint,Loan
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
import time
import string
import random
# Create your views here.
@login_required
def home(request):
    customerObj = request.user.customer
    return render(request, 'users/home.html', {'balance': customerObj.amount})


@login_required
def about(request):
    return render(request, 'users/about.html')


@login_required
def newTransaction(request):
    if request.method == 'POST':
        form = NewTransactionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            print(username)
            amount = form.cleaned_data.get('amount')
            sender = request.user
            if sender.customer.amount >= amount:
                print('amount')
                if User.objects.filter(username=username):
                    print('filter')
                    sender.customer.amount -= amount
                    receiver = User.objects.filter(username=username).first()
                    receiver.customer.amount += amount
                    sender.customer.save()
                    receiver.customer.save()
                    success = True
                    messages.success(
                        request, f'Sucessfully transferred to {username}')
                else:
                    messages.warning(request, f'No user exists')
                    return HttpResponseRedirect(reverse('users:new-transaction'))
            else:
                success = False
                messages.warning(
                    request, f'Transaction failed:Insufficient Funds')
            txnobject = Transaction(transactionID=''.join(random.choices(string.ascii_letters + string.digits, k=15)), transactionAmount=amount,
                                    transactionFrom=sender, transactionTo=User.objects.filter(username=username).first(), success=success)
            txnobject.save()
            if(success):
                return HttpResponseRedirect(reverse('users:home'))
            else:
                return HttpResponseRedirect(reverse('users:new-transaction'))
    else:
        form = NewTransactionForm()

    return render(request, 'users/new_transaction.html', {'form': form})


@login_required
def complaintCreateView(request, **kwargs):
    if request.method == 'POST':
        form = ComplaintCreationForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            complaintObj=Complaint(complaintID=''.join(random.choices(string.ascii_letters + string.digits, k=15)),
                      complaintUser=request.user,
                      transaction=Transaction.objects.all().filter(transactionID=kwargs['transactionID']).first(), 
                      text=text, )
            complaintObj.save()
            messages.success(
                        request, f'Complaint Raised Sucessfully')
            return HttpResponseRedirect(reverse('users:my-transactions'))
        else:
            form=ComplaintCreationForm()
    else:
        form=ComplaintCreationForm()

    return render(request,'users/complaint_creation.html',{'form':form})


@login_required
def applyLoanView(request):
    if request.method=='POST':
        form=ApplyLoanForm(request.POST)
        if form.is_valid():
            loanUser=User.objects.all().filter(username=request.user.username).first()
            print(loanUser)
            loanAmount = form.cleaned_data.get('loanAmount')
            loanAbout = form.cleaned_data.get('loanAbout')
            loanCustomer=loanUser.customer
            loanCustomer.amount+=loanAmount
            loanCustomer.save()
            loanObj=Loan(loanID=''.join(random.choices(string.digits, k=15)),
                loanUser=loanUser,
                loanAmount=loanAmount,
                loanAbout=loanAbout)
            loanObj.save()
            messages.success(
                        request, f'Loan Sanctioned Sucessfully')
            return HttpResponseRedirect(reverse('users:home'))
    else:
        form=ApplyLoanForm()
    return render(request,'users/apply_loan.html',{'form':form})




class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    context_object_name = 'transactions'
    ordering = ['-dateTime']

    def get_queryset(self):
        queryset = super().get_queryset()
        transactions = list(queryset.filter(transactionFrom=self.request.user))
        transactions += list(queryset.filter(transactionTo=self.request.user))
        #loans=Loan.objects.filter(loanUser=self.request.user)
        #transactions+=list(loans)
        return transactions


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Customer
    fields = ['username']

    def get_object(self, **kwargs):
        user = None
        user = User.objects.filter(username=self.kwargs['username']).first()
        return get_object_or_404(Customer, user=user)


class TransactionDetailView(LoginRequiredMixin, DetailView):
    model = Transaction
    context_object_name = 'transaction'

    def get_object(self, **kwargs):
        return get_object_or_404(Transaction, transactionID=self.kwargs['transactionID'])

class MyComplaintListView(LoginRequiredMixin,ListView):
    model=Complaint
    context_object_name='complaints'


    def get_queryset(self):
        queryset=Complaint.objects.all()
        complaints=queryset.filter(complaintUser=self.request.user)
        return complaints


class MyLoanListView(LoginRequiredMixin,ListView):
    model=Loan
    context_object_name='loans'


    def get_queryset(self):
        queryset=Loan.objects.all()
        loans=queryset.filter(loanUser=self.request.user)
        return loans 
