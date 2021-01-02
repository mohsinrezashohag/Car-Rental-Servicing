from django.shortcuts import render,get_object_or_404
from .models import Car_Listings
from django.conf.urls.static import static
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator





def Carlist(request):

    carlistings=Car_Listings.objects.order_by('-list_date').filter(is_Available=True)

    paginator = Paginator(carlistings,4) 

    page=request.GET.get('page')


    carlistings=paginator.get_page(page)


    context={

    'carlistings':carlistings,
   
    }   

    return render (request,'carlists/carlist.html',context)




def onecar(request,id):

     onecar=get_object_or_404(Car_Listings, pk=id)

     context={'onecar':onecar}

     return render(request,'carlists/onecar.html',context)


      

