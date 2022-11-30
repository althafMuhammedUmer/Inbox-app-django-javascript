from django.contrib import admin
from .models import Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    readonly_fields = ['name', 'phone', 'email', 'subject', 'message', 'file']
    list_display = ['name', 'phone', 'email', 'subject', 'message', 'created_at', 'situation']
    search_fields = ['name','phone', 'email',  'subject']
    list_filter = ['status']
    list_per_page = 10


admin.site.register(Customer,CustomerAdmin)
