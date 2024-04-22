from django.urls import path

from Book.views import *

urlpatterns = [
    path('List/', ListBook , name='book_list'),
    path('showDetails/<int:id>', showDetail),
    path('delete/<int:id>', deleteBook)

]
