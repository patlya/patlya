from urllib import request
from django.db import models
from django.urls import reverse


# Create your models here.
class Company(models.Model):
    emp_name=models.CharField(max_length=200,null=True,blank=True)
    emp_comy=models.CharField(max_length=200,null=True,blank=True)


    def __str__(self):
        return self.emp_name

class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField()

    def get_absolute_url(self):
        #return f"/products/{self.slug}/"
        return reverse('first_app:detail',args=[self.id,])
