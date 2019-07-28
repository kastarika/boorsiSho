from django.urls import path

from . import views

urlpatterns = [
    path('search',views.searching),
    path('1/<companyName>/',views.showName, name='showName'),
    path('', views.showAll, name='showAll'),
]