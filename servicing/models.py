from django.db import models
from datetime import datetime
from django.urls import reverse


# Create your models here.


class Our_services(models.Model):

  title=models.CharField(max_length=50,default=None)
  description=models.CharField(max_length=50)
  image=models.ImageField(upload_to='images/',blank=True)
  list_date=models.DateTimeField(default=datetime.now,blank=True)
    
 

  
  def __str__(self):
      return self.title

  