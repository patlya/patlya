from django.urls import path

from first_app.models import Product

from .import views

app_name='first_app'

#temprery url created 
urlpatterns = [
    path('xy/', views.index,{'name': 'abc'}), #{'name':'xyz'}
    # path('company/',views.comp_emp),#name='news-year-archive'
    # path('python/',views.python),
    # path('django/',views.home,name='xyz'),
    # path('about/',views.home,name='aboutus'),

    #path('<int:timeframe>/', views.goals_by_int_timeframe),
    #path('<str:timeframe>/', views.goals_by_timeframe, name='namedurl'),
    path('a/',views.geeks_view, name='template1'),
    path('b/',views.vav_view, name='template2'),
    path('c/',views.list_view),
    path('ranu/',views.my_view,name='abc'),
    path('pr/', views.product_view,name='pro'),
    path('<int:id>/', views.product_detail,name='detail'),
    path('z/', views.http_404_fun),
]