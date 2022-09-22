from django.urls import path

from . import views

urlpatterns = [
    # path('show-basic/', views.show),
    # path('student/<int:student_id>/',views.student),
     path("detail",views.detail)
    
]