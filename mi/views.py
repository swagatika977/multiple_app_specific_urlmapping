from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def yuraj(request):
    return render(request,'yuraj.html')
def shreyesh(request):
    return HttpResponse('<h1>gd players</h1>')
