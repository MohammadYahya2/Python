from django.shortcuts import render,HttpResponse,redirect
from .models import users
def index(request):
    context = {
        "Users" : users.objects.all()


}


    return render(request,"index.html",context)


