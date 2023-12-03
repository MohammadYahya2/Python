from django.shortcuts import render
from flask import redirect
from.models import Book,Author
def index(request):
    context ={

"Book" : Book.objects.all(),
    }
    return render(request,"index.html",context)
def show(request):
    title =request.POST['title'] 
    desc =request.POST['desc']
    Book.objects.create(title=title, desc=desc)
    return redirect("/")


def view_book(request,id):
    Book = Book.objects.get(id=id)
    Authors = Book.Authors.all()
    Books_authors = Author.objects.get(books=Book)
    context = {
        "Books": Book,
        "authors": Authors,
        " Books_authors":  Books_authors
    }
    return render(request, "show.html", context)
