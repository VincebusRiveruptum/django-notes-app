from email import message
import json
from django.core.mail.message import utf8_charset
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from notes.forms.notes import NoteForm
from notes.models import Book, Note
from django.views.decorators.http import require_http_methods

# Create your views here.

# Notes index
def index(request, book_id: int):
    book = Book.objects.get(pk=book_id)

    notes = book.notes.all()

    paginator = Paginator(notes, per_page=10)
    page_number = request.GET.get("page")
    paginated_notes = paginator.get_page(page_number)

    return render(
        request,
        template_name="notes/index.html",
        context={
            'book': book,
            'notes': paginated_notes,
        }
    )

def show(request, book_id:int, note_id:int):
    book = Book.objects.get(pk=book_id)
    note = Note.objects.get(pk=note_id)

    return render(
        request,
        template_name='notes/show.html',
        context={
            'book': book,
            'note': note
        }
    )

def delete(request, book_id: int, note_id: int):
    note = get_object_or_404(Note, id=note_id)
    note.delete()

    return JsonResponse({
        'success': True,
        'message' : "Note deleted successfully"
    })

def edit(request, note):
    print("TODO: Implement update")

    note = Note.get(pk=note.id)
    return render(
        request,
        template_name="notes/edit.html",
        context={
            "note" : note
        }
    )

def create(request, book_id: int):
    book = Book.objects.get(pk=book_id)

    if request.method == "POST":
        form = NoteForm(request.POST)

        if form.is_valid():
            note = form.save(commit=False)
            note.book = book
            note.save()
            return redirect("views.notes.index", book_id=book.id)
    else:
        form = NoteForm()

    return render(
        request=request,
        template_name="notes/create.html",
        context={
            'form': form,
            'book': book
        }
    )

@require_http_methods(["POST"])
def highlight(request, note_id: int, book_id: int):
    data = json.loads(request.body)
    note = get_object_or_404(Note,id=note_id)

    note.highlight = data.get('highlighted', True)
    note.save(update_fields=['highlight'])

    return JsonResponse({
        'success': True,
        'message': "Note updated successfully"
    })
