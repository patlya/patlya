from django.db import models


class Service(models.Model):
    serv_icon=models.CharField(max_length=200)
    serv_title=models.CharField(max_length=50)
    serv_dis=models.TextField()


    

# Create your models here.
