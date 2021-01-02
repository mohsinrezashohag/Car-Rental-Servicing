from django.urls import path
from .views import Carlist,onecar
from . import views

urlpatterns = [
    path('', views.Carlist,name='carlists'),
    path('<int:id>', views.onecar, name="onecar"),
 
   
]
