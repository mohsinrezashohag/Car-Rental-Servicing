from django.urls import path
from . import views


urlpatterns = [
    path('',views.services,name='servicing'),
    path('<int:id>',views.service_details,name='service_details')

]
