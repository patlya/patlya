from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from.models import *

def django_fees(request):
    return HttpResponse('3000')