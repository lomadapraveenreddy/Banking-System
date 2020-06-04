from django.contrib import admin
from .models import Transaction,Customer,Complaint,Loan,DebitCard


admin.site.register(Transaction)
admin.site.register(Customer)
admin.site.register(Complaint)
admin.site.register(Loan)
admin.site.register(DebitCard)