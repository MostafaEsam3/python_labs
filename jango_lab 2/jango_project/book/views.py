from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.http import  HttpResponse
from book.models import *
from .forms import *

from .forms import *
def hello(request):
    return HttpResponse('<h1>hello veiw book</h1>')
def listBooks(request):
    books=Book.objects.all()
    context={'books':books}

    return render(request,'book/list.html',context)
    #return  HttpResponse('<h1>List book</h1>')
def book_addmodel(requst):
    context={'form':addBookModel()}
    return render(requst,'book/add.html',context)


def book_ModelForm(request):
    context={'form':addBookModel()}
    if (request.method == 'POST'):
        form=addBookModel(data=request.POST,files=request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('list_book')
    #     # save data in model
    #     if (len(req.POST) > 0 and len(req.POST['title']) > 3 and req.POST['author'] != None):
    #         Book.objects.create(title=req.POST['title'], author=Author.getauthorbyid(req.POST['author']))
    #         return redirect('book_list')
    #     else:
    #         # print("1")
    #         context['msg'] = "please fill all data"
    #     # return HttpResponse("<h1>Book_Add</h1>")
    #     # print(context['msg'])
    return render(request, 'book/add.html',context)
def add_book(request):
    context={'form':Addbook()}
    if(request.method=='POST'):
            if(len(request.POST)>0 and request.POST['title']!=None):
                Book.objects.create(title=request.POST['title'],
                                     author=Author.getauthorbyid(request.POST['author']))
                return HttpResponseRedirect(reverse('list_book'))
            else:
                context['msg']='all fill fileds'
    return render(request,'book/add.html',context)

    #return  HttpResponse('<h1>Add  book</h1>')
def update_book(request,id):
        book_instance = Book.objects.get(id=id)
        if request.method == 'POST':
            form = addBookModel(request.POST, request.FILES, instance=book_instance)
            if form.is_valid():
                form.save()
                return redirect('list_book')
        else:
            form = addBookModel(instance=book_instance)
        context = {'form': form}
        return render(request, 'book/update.html',context)
   # return  HttpResponse('<h1>Update book</h1>')
def delete_bookId(request,id):
    Book.objects.filter(id=id).delete()
    return redirect('list_book')

def details_bookId(request, id):
    context = {}
    book = Book.objects.get(id=id)
    context['book'] = book
    return render(request, 'book/details.html', context)

    ##return HttpResponse(f'<h1>delete book {id}</h1>')