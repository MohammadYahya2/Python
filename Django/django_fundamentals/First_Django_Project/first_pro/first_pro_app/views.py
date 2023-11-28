from django.shortcuts import render, redirect

def root(request):
    return redirect("/blogs")

def index(request):
    message = "placeholder to later display a list of all blogs"
    return render(request, "index.html", {"message": message})

def new(request):
    message = "placeholder to display a new form to create a new blog"
    return render(request, "new.html", {"message": message})

def create(request):
    return redirect('/')

def show(request, id):
    message = f"placeholder to display blog number {id}"
    return render(request, "show.html", {"message": message})

def edit(request, id):
    message = f"placeholder to edit blog {id}"
    return render(request, "edit.html", {"message": message})

def destroy(request):
    return redirect("/blogs")
