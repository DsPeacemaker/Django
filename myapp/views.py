from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

def index(request):
    books = Book.objects.all()
    context = {'books': books}
    retrun render(request, 'index.html', context)
