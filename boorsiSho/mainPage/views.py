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

def showName(request, companyId):
    return render(request,'mainPage/showName.html', { 'company':Company.objects.get(pk=companyId) })

def showAll(request):
    return render(request, 'mainPage/showAll.html', {'allCompanies':Company.objects.all()})