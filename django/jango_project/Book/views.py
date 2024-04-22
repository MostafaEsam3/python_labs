from django.shortcuts import render

from django.http import HttpResponse

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
from .models import *

def ListBook(request):
    books=Book.objects.all()

    return render(request,'Book/list.html',context={'books':books})


def showDetail(request,id):
    oneBook=Book.objects.get(id=id)

    return render(request,'Book/oneBook.html',context={'oneBook':oneBook})

def deleteBook(request,id):
    book=Book.objects.get(id=id)
    book.delete()
    return redirect('book_list')
