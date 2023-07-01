from django.db import models
import datetime
from django.utils.timezone import now


# Create your models here.
class seller(models.Model):
    name = models.CharField(max_length=50,default="paidipeddi ramakrishna")
    address = models.CharField(max_length=150,default="srikakulam, AP")
    phone = models.CharField(max_length=20,default='+91 9121862212')
    date = models.DateField(default=now())

class buyer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=50)
    purchase_date = models.DateField(default=now())
    quantity=models.IntegerField(default=1)

class products(models.Model):
    img = models.ImageField(upload_to='media/')
    name = models.CharField(max_length=100)
    dis = models.TextField(max_length=500)
    price = models.CharField(max_length=100)


class rk(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()