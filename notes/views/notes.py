from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render

from notes.models import Note

# Create your views here.

# Notes index
def index(request):
    notes = Note.objects.all()

    paginator = Paginator(notes, per_page=10)
    page_number = request.GET.get("page")
    paginated_notes = paginator.get_page(page_number)

    return render(
        request,
        template_name="notes/index.html",
        context={
            'notes': paginated_notes,
        }
    )

def show(request, note):
    note = Note.get(note)

    return render(
        request,
        template_name='notes/show.html',
        context={
            'note': note
        }
    )

def delete(request, note):
    note = Note.get(note)
    note.delete()

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

def create(request):
    print("TODO: Implement create view")

    return render(
        request=request,
        template_name="notes/create.html",
    )