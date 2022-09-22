from urllib import response
from django import http

from django.http import HttpResponse

def hello():
    name="hello"
    return HttpResponse(name)