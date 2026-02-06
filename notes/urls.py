from django.urls import path
from .views import (
    NotesListCreateView, NoteDetailView,
)

urlpatterns = [
    path("notes/", NotesListCreateView.as_view(), name="notes-list-create"),
    path("notes/<int:pk>/", NoteDetailView.as_view(), name="note-detail"),
]
