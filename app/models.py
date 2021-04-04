from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Contact(models.Model):
    name=models.TextField(max_length=60)
    phone=models.CharField(max_length=60)
    email=models.TextField(max_length=60)
    description=models.TextField()
 
    def __str__(self):
        return self.name
    
class activities(models.Model):
    name=models.TextField(max_length=60)
    description=models.TextField()
    date=models.TextField(max_length=60)
    list=models.TextField(max_length=60)
    root=models.ForeignKey(User ,on_delete=models.CASCADE,default='')
    finish=models.CharField(max_length=5)

    def __str__(self):
        return self.name
    