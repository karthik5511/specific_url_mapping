from django.urls import path
from food.views import *


app_name='karthik'

urlpatterns=[
    path('apple/',apple,name='apple')
]
