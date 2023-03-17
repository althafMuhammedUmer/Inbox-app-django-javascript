from django.shortcuts import render,redirect
# My import
from django.contrib.auth.decorators import login_required # login_required is used to prevent private page
from django.views.decorators.cache import cache_control # cache_control will destroy the session after logout

from .models import Customer
from .forms import CustomerForm
from django.contrib import messages
from django.http import HttpResponseRedirect # this will prevent DDOS attact in your front end inputs by redirecting page and clear all inputs
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q #Global search
from django.core.paginator import Paginator
# from datetime import datetime 
from django.utils.timezone import datetime



    # =============(Frontend)================#
# function to homepage (frontend)
def home(request):
    return render(request, "home.html")

# function to send message 
@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            print('form is valid')
            form.save()
            messages.success(request, 'Message send successfully')
        else:
            print(form.errors)
            
           
        return HttpResponseRedirect('/')
    
    
    else:
        form = CustomerForm()
        
    return render(request, "home.html", {'form':form})
        


    # =============(Backend)================#
# function to inbox (backend)


@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)  # with these three configuratin we distroy the session
def inbox(request):
    if "keyword" in request.GET:
        q = request.GET["keyword"]
        all_customer_list = Customer.objects.filter(
            Q(name__icontains=q) | Q(phone__icontains=q) |
            Q(email__icontains=q) | Q(subject__icontains=q) |
            Q(message__icontains=q) | Q(status__icontains=q) 
            
        ).order_by('-created_at')
    else:  
        all_customer_list = Customer.objects.all().order_by('-created_at')
        
    paginator = Paginator(all_customer_list, 4)
    page = request.GET.get('page')
    all_customer = paginator.get_page(page)
    
    
    # -------------Message Counter --------------- #
    # 1) Total
    total = Customer.objects.all().count()
    
    # 2) read 
    read = Customer.objects.filter(status="Read").count()
    
    # 3) unread
    unread = Customer.objects.filter(status="Pending").count()
    
    # 4) today 
    base = datetime.now().date()
    today = Customer.objects.filter(created_at__gt=base).count()
    
    
    return render(request, "inbox.html", {
        "customers" : all_customer,
        
        "total": total,
        "read": read,
        "unread": unread,
        "today" : today,
    
        })
 
# function to delete customer(message)   
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def delete_customer(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    customer.delete()
    
    messages.success(request, "Message is successfully deleted !")
    
    return HttpResponseRedirect('/inbox')


# function to view customer message individually
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def customer(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    
    if customer != None:
        return render(request, 'customer.html', {"customer": customer})
    
    
    




