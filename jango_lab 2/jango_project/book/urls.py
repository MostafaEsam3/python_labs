from django.urls import path
from .views import *
urlpatterns=[

        path('list/', listBooks, name='list_book'),
        path('add/', add_book, name='add_book'),
        path('addmodel/', book_addmodel, name='book_addmodel'),
        path('add/BookModel/',book_ModelForm,name='book_ModelForm'),
        path('update/<int:id>', update_book, name='update_book'),
        path('details/<int:id>', details_bookId, name='details_bookId'),

        path('delete/<int:id>', delete_bookId,name='delete_bookId'),
  ]