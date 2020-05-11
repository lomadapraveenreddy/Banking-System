from django.contrib import admin
from .models import Transaction,Customer
# Register your models here.

admin.site.register(Transaction)
admin.site.register(Customer)