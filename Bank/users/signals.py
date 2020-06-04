from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Customer,DebitCard
import random,string
from hashlib import sha256
import uuid 

@receiver(post_save,sender=User)
def create_customer(sender,instance,created,**kwargs):
    if created:
        print('customer signal')
        Customer.objects.create(user=instance,\
            accountNumber=str(uuid.uuid4().fields[-1])[:10]).save()
        

@receiver(post_save,sender=User)
def create_debit_card(sender,instance,created,**kwargs):
    if created:
        print('debit card signal')
        DebitCard.objects.create(cardUser=instance,
            cardNumber=str(uuid.uuid4().fields[-1])[:12],
                nameOnCard=instance.username,
                cvv=int(str(uuid.uuid4().fields[-1])[:3]),
                pin=int(str(uuid.uuid4().fields[-1])[:4]),
                    ).save()