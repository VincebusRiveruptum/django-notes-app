from django.forms import ModelForm

from notes.models import Book

class BookForm(ModelForm):
    class Meta:
        model=Book
        fields=["title", "description"]