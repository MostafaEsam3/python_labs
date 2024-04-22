from django.shortcuts import render

from django.http import HttpResponse

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect



def hello(request):
    return HttpResponse('<h1>hhhhhhhhhh</h1>')