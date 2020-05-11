from django.urls import path,include
from . import views

app_name= 'users'
urlpatterns = [
    path('home/',views.home,name='home'),
    path('new_transaction',views.newTransaction,name='new-transaction'),
    path('my_transactions',views.myTransactions,name='my-transaction'),
]
