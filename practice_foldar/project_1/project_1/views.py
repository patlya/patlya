from django.http import HttpResponse
from django.shortcuts import render


#html render
# def home_page(request):
#     return render(request, 'index.html')


#data pass django file to html file
def home_page(request):

    data={
         # view se data transfer html file 
           'title':'Home page new',
           'H_tag':'Welcome to home page',
           'P_tag':'we create html render so firstly we impot django.shortcut from import and render function take two parameter first request and which page create in templets .....!',
             'numbers':[10,20,30,40,50],
            'clist':['java','python','php'],
            'stu_list':[
                    {'name':"Ranu",'phone':'8817214690'},
                    {'name':"sanju",'phone':'8976654455'},
            ],


    }
    return render(request, 'index.html',data)    

def aboutUs(request):
    return HttpResponse("hello this is first views.....!<a href='/'> back </a>")

def show(request):
    return HttpResponse("hy...i am django first text....!!")    



#dynamic rout create
def dynamic_rout(request,dynamicid):
    return HttpResponse(dynamicid)

