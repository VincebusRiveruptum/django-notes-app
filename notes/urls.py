
from django.urls import path

from notes.views import books, notes

urlpatterns = [
    #Book stuff
    path("books", books.index, name="views.books.index"),
    path("books/create}", books.create, name="views.books.create"),
    path("books/<int:book_id>}", books.show, name="views.books.show"),
    # Note stuff
    path("books/<int:book_id>/notes", notes.index, name="views.notes.index"),
    path("books/<int:book_id>/notes/create", notes.create, name="views.notes.create"),
    path("notes/<int:note_id>", notes.edit, name="views.notes.edit"),

]