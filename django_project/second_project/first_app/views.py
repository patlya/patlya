
from turtle import title
from urllib.request import Request

from django.shortcuts import  render,get_object_or_404,redirect

from django.http import Http404, HttpResponse
from.models import *
from django.http import HttpResponseRedirect
from .models import Company
from django.views.generic.list import ListView
from django.urls import reverse


def index(request,name='xyz'):
    
    return HttpResponse(f"Hello, this is demo of django view.......!!{name}")


def comp_emp(request):
    a=10+20
    return HttpResponse(f' this is result {a}')   

# def python(request):
#     cname='Django'
#     detail={'nm':cname,'Fees':'2000','Duration':'4 month'}
#     return render(request,'index.html' ,context=detail)     


# def home(request):
#     return render(request,'djangos.html')

# def about(request):
#     return render(request,'about.html')


goals={
    'daily':'learn Something New',
    'weekly':'Take a day off',
    'monthly':'complete a createvity'

} 
def goals_by_int_timeframe(request,timeframe):
    timeframes=list(goals.keys())
    redirect_to=timeframes[timeframe-1]
    named_redirect=reverse('namedurl',args=[redirect_to])
    return HttpResponseRedirect(named_redirect)


# def goals_by_timeframe(request, timeframe):
#     goal = goals[timeframe]
#     html = "<html><body>It is now %s.</body></html>"
#     return HttpResponse(goal)  


def geeks_view(request):
    context = {
        # 'data':[1,2,3,4,5,6,6,7,8],
        'data':99
    }
    return render(request,'index.html',context) 


def vav_view(request):
   return render(request,'about.html') 



#-------function based view----------------
def list_view(request):
    context ={}
    context["dataset"] = Company.objects.all()    
    return render(request, "djangos.html", context)

def my_view(request):
    # obj=Company.objects.get(id=1) 
    return  redirect('abc',nm='yes')


#-------we use two methods get_absolute_url and get_objects_or_404
def product_view(request):
    obj_list=Product.objects.all()
    return render(request,'get_absolut.html',{'obj_list':obj_list})

def product_detail(request,id):
    obj=get_object_or_404(Product,pk=id, title__startswith='a')
    return render(request,'detail.html',{'obj':obj})
        
def http_404_fun(request):
    #ps=get_object_or_404(Product,pk=4)
    try:
        pr=Product.objects.get(id=3)
    except Product.DoesNotExist:
        raise Http404("given id is not availabel in database ")
    return HttpResponse("hello")