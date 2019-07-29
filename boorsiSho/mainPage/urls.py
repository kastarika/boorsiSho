app_name = "mainPage"

from django.urls import path

from . import views

urlpatterns = [
    path('<int:companyId>/',views.showName, name='showName'),
    path('', views.showAll, name='showAll'),
]