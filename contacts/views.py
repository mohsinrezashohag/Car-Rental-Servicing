from .models import Car_Request,Service_Request
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def car_contact(request):

   
    if request.method == 'POST':

       car_name=request.POST['onecar']
       user_id=request.POST['user_id']
       car_id=request.POST['car_id']
       name=request.POST['name']
       email=request.POST['email']
       phone=request.POST['phone']
       message=request.POST['message']



       if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted=Car_Request.objects.all().filter(user_id=user_id,car_id=car_id)

            if has_contacted:
                messages.error(request, 'You have already has contact for this ')
                return redirect('dashboard')
        
       
       
       car_contact=Car_Request(car_name=car_name,name=name,email=email,phone=phone,message=message,user_id=user_id,car_id=car_id)

       car_contact.save()

       messages.success(request,'Your Request has been submited.We will contact you soon')

       

       return redirect('dashboard')


      











@login_required
def servicing_contact(request):

   
    if request.method == 'POST':

       service_name=request.POST['title']
       user_id=request.POST['user_id']
       service_id=request.POST['service_id']
       name=request.POST['name']
       email=request.POST['email']
       phone=request.POST['phone']
       problem_shortly=request.POST['problem_shortly']



       if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted=Service_Request.objects.all().filter(user_id=user_id,service_id=service_id)

            if has_contacted:
                messages.error(request, 'You have already has contact for this service ')
                return redirect('dashboard')

       
       
       service_contact=Service_Request(name=name,email=email,phone=phone,problem_shortly=problem_shortly,user_id=user_id,service_id=service_id,service_name=service_name)

       service_contact.save()

       messages.success(request,'Your Request has been submited.We will contact you soon')

       

       return redirect('dashboard')