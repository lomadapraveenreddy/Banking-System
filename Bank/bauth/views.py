from django.shortcuts import render,reverse
from .forms import UserRegisterForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,'bauth/home.html',{})



def register(request):

    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account is Sucessfully Created for {username}',)
            form.save()
            return HttpResponseRedirect(reverse('bauth:login'))
    else:
        form=UserRegisterForm()
    return render(request,'bauth/register.html',{'form':form,})
