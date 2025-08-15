
from django.urls import path

from notes import views

urlpatterns = [
    path("", views.index, name="views.index"),
    path("create", views.create, name="views.create")
]