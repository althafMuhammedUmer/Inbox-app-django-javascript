from django.db import models
from django.utils.html import format_html

# Create your models here.
class Customer(models.Model):
    
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=1000)
    file = models.FileField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
    
    
    # control read/unread message in admin.py
    def situation(self):
        if self.status == 'Read':
            return format_html('<span style="color: green">{0}</span>', self.status)
        else:
            return format_html('<span style="color: red">{0}</span>', self.status)
    situation.allow_tags = True
    
    def __str__(self):
        return self.name
        
        
            
    
    
    
