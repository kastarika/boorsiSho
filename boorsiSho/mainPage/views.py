from django.shortcuts import render
from django.http import HttpResponse
from .models import Company, FinancialRatio
# Create your views here.

'''def fillInDatabase( request ):
    readFromDatabase.fillInDatabase()
    return HttpResponse("DONE")
   ''' 

def searching(request):
    return render(request,'mainPage/Page1.html')

def showName(request, companyId):
    currentCompany = Company.objects.get( pk=companyId )
    currentFinancialRatio = FinancialRatio.objects.filter( company=currentCompany ).latest( 'dateCreated' )
    return render(request,'mainPage/showName.html', { 'company':currentCompany, 'financialRatio':currentFinancialRatio })

def showAll(request):
    return render(request, 'mainPage/showAll.html', {'allCompanies':Company.objects.all()})