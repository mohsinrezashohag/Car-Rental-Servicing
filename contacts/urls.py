from django.urls import path
from . import views


urlpatterns = [
    path('',views.car_contact,name='car_contact'),
    path('contact/',views.servicing_contact,name='servicing_contact')
]


