from mi.views import *
from django.urls import path
app_name='something'
urlpatterns=[
    path('yuraj/',yuraj,name='yuraj'),
    path('shreyesh/',shreyesh,name='shreyesh'),
]