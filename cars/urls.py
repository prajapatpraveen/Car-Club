from unicodedata import name
from django.urls import path
from . import views
urlpatterns=[
    path('',views.Cars,name='cars'),
    path('<int:id>',views.Car_details, name='car_details'),
    path('search/',views.Search, name='search'),
]