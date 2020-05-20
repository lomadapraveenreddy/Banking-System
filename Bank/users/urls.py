from django.urls import path,include
from .views import (
    ProfileDetailView,
    TransactionListView,
    TransactionDetailView,
)
from . import views

app_name= 'users'
urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('new_transaction/',views.newTransaction,name='new-transaction'),
    path('my_transactions/',TransactionListView.as_view(template_name='users/my_transactions.html'),name='my-transactions'),
    path('transaction/<transactionID>/',TransactionDetailView.as_view(template_name='users/detailed_transaction_view.html'),name='detail-transaction'),
    path('profile/<username>/',ProfileDetailView.as_view(template_name='users/profile.html'),name='profile'),
    
]
