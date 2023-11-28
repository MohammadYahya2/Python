from django.shortcuts import render, redirect
from.models import Show


def root(request):

    context ={

"shows" : Show.objects.all()

    }
    return render(request,"index.html",context)



def NewForm(request):

    return render(request,'NewForm.html')

def shows_create(request):
    title =request.POST['title']
    network =request.POST['Network']
    release_date =request.POST['Date']
    description =request.POST['Dec']
    this_show = Show.objects.create(title = title, network = network, release_date = release_date, description = description)
    return redirect(f"/shows/{this_show.id}")


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
    show_update.title = request.POST['title']
    show_update.network =request.POST['Network']
    show_update.release_date= request.POST['Date']
    show_update.description=request.POST['desc']
    show_update.save()


    return redirect(f'/shows/{show_update.id}')

def delete(request , id):
    show =Show.objects.get(id=id)
    show.delete()
    return redirect('/shows')