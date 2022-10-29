from django.shortcuts import render,redirect
# My import
from django.contrib.auth.decorators import login_required # login_required is used to prevent private page
from django.views.decorators.cache import cache_control # cache_control will destroy the session after logout




# function to homepage (frontend)
def home(request):
    return render(request, "home.html")

# function to inbox (backend)
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)  # with these three configuratin we distroy the session
def inbox(request):
    return render(request, "inbox.html")

