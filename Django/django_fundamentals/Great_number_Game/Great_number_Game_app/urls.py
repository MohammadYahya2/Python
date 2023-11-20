from django.urls import path
from . import views

urlpatterns=[
    path('',views.root),
    path('check_guess',views.check_guess)
]