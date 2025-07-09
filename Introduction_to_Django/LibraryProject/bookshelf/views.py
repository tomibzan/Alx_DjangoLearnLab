from django.shortcuts import render
from django.http import HttpResponse


def bookshelf(request):
    return HttpResponse("Welcome to the Bookshelf!")


# Create your views here.
