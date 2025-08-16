
from os import name
from django.core.paginator import Paginator
from django.shortcuts import redirect, render

from notes.forms.books import BookForm
from notes.models import Book


def index(request):
    books = Book.objects.all()
    paginator = Paginator(books, per_page=10)
    current_page = request.GET.get("page")
    books_paginated = paginator.get_page(current_page)

    return render(
        request,
        template_name="books/index.html",
        context={
            'books': books_paginated
        }
    )

def show(request, book_id: int):
    book = Book.objects.get(pk=book_id)

    return render(
        request=request,
        template_name="books/show.html",
        context={
            "book": book
        }
    )

def create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(to="views.books.index")
    else:
        form = BookForm()

    return render(
        request=request,
        template_name="books/create.html",
        context={
            "form": form
        }
    )

def edit(request, book_id: int):
    book = Book.objects.get(pk=book_id)

    return render(
        request=request,
        template_name="books/edit.html",
        context={
            "book": book
        }
    )

