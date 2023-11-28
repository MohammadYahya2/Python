from django.shortcuts import render,HttpResponse,redirect
from .models import Dojo,Ninja
def index(request):
    
    context = {
    

    "Dojo"  : Dojo.objects.all()
}

    return render(request,"index.html",context)



def Dojo1(request):

    name=request.POST['name']  
    city=request.POST['city']  
    state=request.POST['state']
    Dojo.objects.create(name=name,city=city,state=state)
    return(redirect("/"))
def Ninja2(request):
    MY_Ninja=Ninja.objects.create(
    first_name=request.POST['FirstName']
    ,last_name=request.POST['LastName'],
    dojo=Dojo.objects.get(name= request.POST.get('dojo',False)))
    return(redirect("/"))

