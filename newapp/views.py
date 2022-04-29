from django.shortcuts import render
from django.http import HttpResponse

def samplefn(request):
    return HttpResponse('abc')


def heading1(request):
    return render(request,'new.html')



def h1(request):
    return render(request,'h1.html')
      
