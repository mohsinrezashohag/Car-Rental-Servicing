from django.contrib import admin
from .models import Car_Request,Service_Request

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    
    list_display=('id','name','car_name','email','contact_date','confirm')
    list_display_links=('id','name')
    search_fields=('name','email','car_name')
    list_editable=('confirm',)
    list_per_page=25


class Servicing_ContactAdmin(admin.ModelAdmin):
     
     list_display=('service_name','name','email','problem_shortly','confirm')
     list_display_links=('name','service_name')
     list_editable=('confirm',)
     list_per_page=25


admin.site.register(Car_Request,ContactAdmin)



admin.site.register(Service_Request,Servicing_ContactAdmin)