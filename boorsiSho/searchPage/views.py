from django.shortcuts import render
from mainPage.models import Company
from django.http import HttpResponse, JsonResponse

# Create your views here.

'''def search( request ):
    if request.method == 'POST':
        searchKeyWord = request.POST['searchKeyWord']
        companyList = Company.objects.filter( name__icontains=searchKeyWord )
        return render( request, 'searchPage/showSearchResult.html', { 'companyList':companyList } )
    else:
        return render( request, 'searchPage/getSearchQuery.html' )
'''

def search( request ):
    if request.method == 'POST' and request.is_ajax():
        searchKeyWord = request.POST[ 'searchKeyWord' ]
        companyList = Company.objects.filter( name__icontains=searchKeyWord )
        return JsonResponse( {'companyList':companyList} )
