
from django.shortcuts import render,HttpResponse,redirect
from .models import users
def index(request):
    context = {
        "users" : users.objects.all()

}

    return render(request,"index.html",context)

def addUsers(request):
    First_Name = request.POST['add']  
    Last_Name = request.POST['add-1']  
    Email = request.POST['add-2']  
    Age = request.POST['add-3']  
    users.objects.create(first_name=First_Name,last_name=Last_Name,email_address=Email,age=Age)
    return(redirect("/"))