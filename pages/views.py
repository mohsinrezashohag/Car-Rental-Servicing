from django.http.response import HttpResponse
from django.shortcuts import render
from carlists.models import Car_Listings
from servicing.models import Our_services







def home(request):   

    return render(request,'pages/home.html')





def about(request):
    return render(request,'pages/about.html')









def service_pricing(request):

    cars_info=Car_Listings.objects.all()
    servicing_info=Our_services.objects.all()

    context={'cars_info':cars_info,
    'servicing_info':servicing_info
    }

    return render(request,'pages/pricing_table.html',context)




