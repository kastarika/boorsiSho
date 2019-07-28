from django.urls import path

from . import views

urlpatterns = [
    path('search',views.searching),
    path('<int:companyId>/',views.showName, name='showName'),
    path('', views.showAll, name='showAll'),
]