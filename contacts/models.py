from django.db import models
from datetime import datetime
from django.shortcuts import get_object_or_404

# Create your models here.


class Car_Request(models.Model):


    car_id=models.IntegerField(null=True)
    car_name=models.CharField(max_length=50)
    user_id=models.IntegerField(null=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    message=models.TextField(blank=True)
    contact_date=models.DateTimeField(default=datetime.now,blank=True)
    confirm=models.BooleanField(default=False)
    user_id=models.IntegerField(null=True)
   
    def __str__(self) :
        return self.name




class Service_Request(models.Model):
    service_name=models.CharField(max_length=50)
    service_id=models.IntegerField(null=True)   
    user_id=models.IntegerField(null=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    problem_shortly=models.TextField(blank=True)
    contact_date=models.DateTimeField(default=datetime.now,blank=True)
    confirm=models.BooleanField(default=False)
    
    def __str__(self) :
        return self.name

   



