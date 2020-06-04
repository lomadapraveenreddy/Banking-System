from django.urls import path,include
from .views import (
    ProfileDetailView,
    TransactionListView,
    TransactionDetailView,
    MyComplaintListView,
    MyLoanListView,
    DetailDebitCardView,
)
from . import views

app_name= 'users'
urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('new_transaction/',views.newTransaction,name='new-transaction'),
    path('my_transactions/',TransactionListView.as_view(template_name='users/my_transactions.html'),name='my-transactions'),
    path('my_complaints/',MyComplaintListView.as_view(template_name='users/my_complaints.html'),name='my-complaints'),
    path('loan/',views.applyLoanView,name='apply-loan'),
    path('my_loans/',MyLoanListView.as_view(template_name='users/my_loans.html'),name='my-loans'),
    path('my_debit_card/',DetailDebitCardView.as_view(template_name='users/debit_card_view.html'),name='my-debit-card'),
    path('transaction/<transactionID>/',TransactionDetailView.as_view(template_name='users/detailed_transaction_view.html'),name='detail-transaction'),
    path('createcomplaint/<transactionID>',views.complaintCreateView,name='create-complaint'),
    path('profile/<username>/',ProfileDetailView.as_view(template_name='users/profile.html'),name='profile'),
    

]
