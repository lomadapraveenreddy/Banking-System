from django.contrib import admin
from .models import Transaction,Customer,Complaint


admin.site.register(Transaction)
admin.site.register(Customer)
admin.site.register(Complaint)