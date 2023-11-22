from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def result(request):
    name = request.POST['username']
    location = request.POST['location']
    fav = request.POST['language']
    comment = request.POST['Comment']


    context = {
        "name": name,
        "location": location,
        "fav": fav,
        "comment": comment,
    }
    return render(request,'result.html',context)
