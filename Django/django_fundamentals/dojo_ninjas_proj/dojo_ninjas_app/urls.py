from django.urls import path , include 
from . import views

urlpatterns = [
    path('' ,views.index),
    path('Dojo',views.Dojo1),
    path('Ninja',views.Ninja2),
]