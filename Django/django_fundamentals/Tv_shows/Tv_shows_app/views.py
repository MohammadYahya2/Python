from django.shortcuts import render, redirect,HttpResponse
from .models import Show
from django.contrib import messages

def root(request):
    return redirect('/shows')

def allshows(request):
    context ={
        "shows" : Show.objects.all()
    }
    return render(request,"index.html",context)

def NewForm(request):
    return render(request,'NewForm.html')

def shows_create(request):
    # if  request.method=='POST':
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/shows/create")
        else:
            title = request.POST['Title']
            network =request.POST['Network']
            release_date =request.POST['Date']
            description =request.POST["description"]
            this_show = Show.objects.create(Title = title, network = network, release_date = release_date, description = description)
            this_show.save()
            messages.success(request, "shows successfully updated")
            id =Show.objects.last().id
            return redirect(f'/shows/{id}')
        
    # print(request.POST['Title'])
    # errors = Show.objects.basic_validator(request.POST)
    # if len(errors) > 0:
    #     for key, value in errors.items():
    #         messages.error(request, value)
    #     return redirect("/shows/create")
    # else:
    #     network =request.POST['Network']
    #     release_date =request.POST['Date']
    #     description =request.POST["description"]
    #     this_show = Show.objects.create(title = request.POST['title'], network = network, release_date = release_date, description = description)
    # this_show.save()
    # messages.success(request, "shows successfully updated")
    # return redirect('/shows',Show.objects.last().id)


def showDetail(request , id):
    this_show = Show.objects.get(id=id)
    context ={
        "this_show" : this_show
    }
    return render(request,"showDetail.html",context)


def editing(request , id):
    this_show = Show.objects.get(id=id)
    
    context ={

"this_show" : this_show


    }
    
    
    return render(request,"editform.html",context)


def update(request ,id ):

    show_update=Show.objects.get(id=id)
    show_update.title = request.POST['Title']
    show_update.network =request.POST['Network']
    show_update.release_date= request.POST['Date']
    show_update.description=request.POST['desc']
    show_update.save()


    return redirect(f'/shows/{show_update.id}')

def delete(request , id):
    show =Show.objects.get(id=id)
    show.delete()
    return redirect('/shows')