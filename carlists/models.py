from django.db import models
from datetime import datetime
from django.urls import reverse

from django.db.models.enums import Choices

# Create your models here.


class Car_Listings(models.Model):

    

    title=models.CharField(max_length=50)
    type=models.CharField(max_length=50,)
    seats=models.IntegerField()
    rent_perday=models.IntegerField()
    extra_message=models.CharField(max_length=80)
    photo_main=models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1=models.ImageField(upload_to='photos/%Y/%m/%d/' ,blank=True)
    photo_2=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)   
    is_Available=models.BooleanField(default=True)
    list_date=models.DateTimeField(default=datetime.now,blank=True)
    

    def __str__(self):
        return self.title

    
    
   