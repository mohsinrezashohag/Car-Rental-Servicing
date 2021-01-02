from django.shortcuts import render,get_object_or_404
from .models import Our_services

# Create your views here.


def services(request):
    
    services=Our_services.objects.all()
    
    context={'services':services }
    
    return render(request,'servicing/servicings.html',context)



def service_details(request,id):

    service=get_object_or_404(Our_services, pk=id)

    context={'service':service }
    
    return render(request,'servicing/service_details.html',context)