from django.urls import path
from .views import book_list

#localhost/books
urlpatterns = [
    path('',book_list,name='book_list'),
]