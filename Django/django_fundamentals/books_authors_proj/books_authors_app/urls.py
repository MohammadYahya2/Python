
from django.urls import path , include 
from . import views

urlpatterns = [
    path('' ,views.index),
    path('show' ,views.show),
    path('books/<int:id>',views.view_book),
]
