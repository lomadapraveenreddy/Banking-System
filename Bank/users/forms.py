from django import forms

class NewTransactionForm(forms.Form):
    username=forms.CharField(label='User Name')
    amount=forms.IntegerField(label='Transaction Amout')
    
