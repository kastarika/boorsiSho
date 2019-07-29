app_name = "searchPage"

from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.search, name='getSearchQuery'),
]