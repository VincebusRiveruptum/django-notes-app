
from django.core.paginator import Paginator
from django.shortcuts import render

from notes.models import Book


def index(request):
    books = Book().objects.all()
    paginator = Paginator(books, per_page=10)
    current_page = request.GET.get("page")
    books_paginated = paginator.get_page(current_page)

    return render(
        request,
        template_name="index.html"
        context={
            'books': books_paginated
        }
    )

def show(request, book_id: int):
    book = Book.objects.get(pk=book_id)

    return render(
        request=request,
        template_name="show.html",
        context={
            "book": book
        }
    )


def create(request):
    return render(
        request=request,
        template_name="create.html",
    )


def edit(request, book_id: int):
    book = Book.objects.get(pk=book_id)

    return render(
        request=request,
        template_name="edit.html",
        context={
            "book": book
        }
    )

