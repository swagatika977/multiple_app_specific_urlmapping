from rcb.views import *
from django.urls import path
app_name='anyone'
urlpatterns=[
    path('virat/',virat,name='virat'),
    path('vr/',vr,name='vr'),
]