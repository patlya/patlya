from django.contrib import admin
from .models import  Service

# #(admin.ModelAdmin) ye likhna jaruri he nhi to hme admin pr nhi dikhega ki model ke andr kya likha he 
# class ServiceAdmin(admin.ModelAdmin):
#     list_display=('serv_icon','serv_title','serv_dis')


admin.site.register(Service)   
# Register your models here.
