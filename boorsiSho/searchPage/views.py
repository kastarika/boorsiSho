from django.shortcuts import render
from mainPage.models import Company
from django.http import HttpResponse

# Create your views here.

def search( request ):
    if request.method == 'POST':
        searchKeyWord = request.POST['searchKeyWord']
        companyList = Company.objects.filter( name__icontains=searchKeyWord )
        return render( request, 'searchPage/showSearchResult.html', { 'companyList':companyList } )
    else:
        return render( request, 'searchPage/getSearchQuery.html' )