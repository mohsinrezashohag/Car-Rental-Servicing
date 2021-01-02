from django.shortcuts import redirect, render
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contacts.models import Car_Request,Service_Request


# Create your views here.




def register(request):

    if request.method =='POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        
        
        if password==password2:
           
           
            if User.objects.filter(username=username).exists():

                messages.error(request,'That username is taken')

              
                return redirect('register')

            else:


                if User.objects.filter(email=email).exists():

                    messages.error(request,'That email is being used')
                    return redirect('register')



                else:


                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                   
                   
                    user.save()

                    messages.success(request,'You are now registered and can log in')

                    return redirect('login')

        else:

            messages.error(request, 'Passwors  not match')

            return redirect('register')

    else:

        return render(request,'accounts/register.html')




def login(request):

    if request.method =='POST':

        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,'you are loged in')
            return redirect('home')
        
        else:
            messages.error(request,'invalid credential')
            return redirect('login')
        
      
        
        
    else:

         return render(request,'accounts/login.html')





def logout(request):

    auth.logout(request)

    messages.success(request,'You are not loged in anymore')
    return redirect('home')





def dashboard(request):
     
    
    
    interested_car_details=Car_Request.objects.order_by('-contact_date').filter(user_id=request.user.id)
    interested_servicing_details=Service_Request.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context={

        'interested_car_details':interested_car_details,
        'interested_servicing_details':interested_servicing_details,

        
        }

    return render(request,'accounts/dashboard.html',context)