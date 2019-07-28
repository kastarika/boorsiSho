from django.shortcuts import render
from django.http import HttpResponse
from . import readFromDatabase

# Create your views here.

def fillInDatabase( request ):
    readFromDatabase.fillInDatabase()
    return HttpResponse("DONE")
    