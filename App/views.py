from django.shortcuts import render,redirect
# My import
from django.contrib.auth.decorators import login_required # login_required is used to prevent private page
from django.views.decorators.cache import cache_control # cache_control will destroy the session after logout

from .models import Customer
from .forms import CustomerForm
from django.contrib import messages
from django.http import HttpResponseRedirect # this will prevent DDOS attact in your front end inputs by redirecting page and clear all inputs



    # =============(Frontend)================#
# function to homepage (frontend)
def home(request):
    return render(request, "home.html")

# function to send message 
def send_message(request):
    if request.method == 'POST':
        print("send message is working")
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            print('form is valid')
            form.save()
            messages.success(request, 'Message send successfully')
        else:
            print(form.errors)
            print('form is invalid')
           
        return HttpResponseRedirect('/')
    
    
    else:
        form = CustomerForm()
        
    return render(request, "home.html", {'form':form})
        


    # =============(Backend)================#
# function to inbox (backend)
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)  # with these three configuratin we distroy the session
def inbox(request):
    return render(request, "inbox.html")




