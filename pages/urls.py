from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
     path('s_and_pricing/',views.service_pricing,name='s_and_pricing')
]
