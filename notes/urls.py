
from django.urls import path

from notes.views import notes

urlpatterns = [
    path("", notes.index, name="views.index"),
    path("create", notes.create, name="views.create")
]