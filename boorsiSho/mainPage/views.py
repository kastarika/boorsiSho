from django.shortcuts import render
from django.http import HttpResponse
from .models import Company
# Create your views here.

'''def fillInDatabase( request ):
    readFromDatabase.fillInDatabase()
    return HttpResponse("DONE")
   ''' 

def searching(request):
    return render(request,'mainPage/Page1.html')

def showName(request, companyName):
    return render(request,'mainPage/showName.html', { 'company':Company.objects.get(name=companyName) })

def showAll(request):
    return render(request, 'mainPage/showAll.html', {'allCompanies':Company.objects.all()})