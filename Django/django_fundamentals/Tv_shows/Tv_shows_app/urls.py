
from django.urls import path , include 
from . import views

urlpatterns = [
    path('', views.root),
    path('shows',views.allshows),
    path('shows/new' ,views.NewForm),
    path('shows/create' ,views.shows_create),
    path('shows/<int:id>' ,views.showDetail),
    path('editing/<int:id>',views.editing),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.delete),
    # path('showsing' ,views.showsing),
]
