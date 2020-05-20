from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Customer
import random,string
import uuid 

@receiver(post_save,sender=User)
def create_customer(sender,instance,created,**kwargs):
    if created:
        Customer.objects.create(user=instance,\
            accountNumber=str(uuid.uuid4().fields[-1])[:10]).save()
        