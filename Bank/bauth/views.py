from django.shortcuts import render,reverse
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,'bauth/home.html',{})



def register(request):

    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account is Sucessfully Created for {username}',)
            form.save()
            return HttpResponseRedirect(reverse('bauth:login'))
    else:
        form=UserCreationForm()
    return render(request,'bauth/register.html',{'form':form,})
