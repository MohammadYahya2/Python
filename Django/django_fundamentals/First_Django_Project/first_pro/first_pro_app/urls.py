from django.urls import path , include 
from . import views

urlpatterns = [
    path('' ,views.root),
    path('bolgs' ,views.index),
    path('bolgs/new' ,views.new),
    path('bolgs/create' ,views.create),
    path('blogs/<int:id>' ,views.show),
    path('blogs/<int:id>/edit' ,views.edit),
    path('blogs/<int:id>/delete' ,views.destroy),

    
]
