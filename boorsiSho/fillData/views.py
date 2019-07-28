from django.shortcuts import render
from .readFromDatabase import Import
import django_excel as DE

# Create your views here.

def fillInDatabase(request):
    if request.method == 'POST' and request.FILES[ 'dataSheet' ]:
        Import.fillInDatabase( request.FILES[ 'dataSheet' ].get_sheet() )
    return render(request, 'fillData/readData.html')