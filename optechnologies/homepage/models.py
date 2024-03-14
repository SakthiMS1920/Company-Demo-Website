from django.db import models

# Create your models here.

class registertion(models.Model):
    Firstname=models.CharField(max_length=20,default='')
    Lastname=models.CharField(max_length=20,default='')
    Email=models.EmailField(max_length=20,default='')
    Companyname=models.CharField(max_length=20,default='')
    Companyurl=models.URLField(max_length=20,default='')
    Companysize=models.CharField(max_length=20,default='')
    Phone=models.IntegerField(default='')
    Areaofspecialiasation=models.CheckConstraint
    organisation=models.CharField(max_length=200,default='')
    medias=models.Choices
    comments=models.CharField(max_length=200,default='')
    