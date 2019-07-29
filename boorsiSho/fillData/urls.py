app_name = "fillData"

from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.fillInDatabase, name='fillInDatabase'),
]