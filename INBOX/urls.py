"""INBOX URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from App import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # =============(Backend)================#
    path('admin/', admin.site.urls),
     # path to inbox page (backend)
    path('inbox/', views.inbox, name="inbox"),
    
    #path to delete message
    path('delete-message/<str:customer_id>', views.delete_customer, name="delete_customer" ),
    
    #path to view the message of customer
    path('customer/<str:customer_id>', views.customer, name="customer"),
    
    # path to mark message as read
    path('mark_message', views.mark_message, name="mark_message"), 
   
    
    
    # =============(Frontend)================#
    # path to home page (front end)
    path('', views.home, name="home"),
    #path to login/logout
    path('accounts/', include('django.contrib.auth.urls')),
    #path to send message
    path('send-message', views.send_message, name="send_message"),
    
      
    
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
