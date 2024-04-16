from django.urls import path
from mobiles.views import *

app_name='sonu'

urlpatterns=[
    path('iphone/',iphone,name='iphone'),
    
]
