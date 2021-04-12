from django.shortcuts import render
from django.http import HttpResponse
def TestFn(request):
    return HttpResponse('helooooo')
def html1(request):
    return render(request,'login.html')

# Create your views here.
