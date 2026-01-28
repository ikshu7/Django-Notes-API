from django.urls import path
#from .views import get_notes, create_notes, note_details, category_list, tag_list
#from .views import NotesList, NoteDetail, CategoryList, TagList
from .views import (
    NotesListCreateView, NoteDetailView,
    CategoryListCreateView, CategoryDetailView,
    TagListCreateView, TagDetailView
)

urlpatterns = [
    # path('notes/', get_notes, name = 'get-notes'),
    # path('notes/create', create_notes, name = 'create-notes'),
    # path('notes/<int:pk>', note_details, name = 'note-details'),
    # path('categories/', category_list, name = 'category-list'),

    # path('tags/', tag_list, name = 'tag-list'),
    # path('notes/', NotesList.as_view(), name='notes-list'),
    # path('notes/<int:pk>/', NoteDetail.as_view(), name='note-detail'),
    # path('categories/', CategoryList.as_view(), name='category-list'),
    # path('tags/', TagList.as_view(), name='tag-list'),

    path("notes/", NotesListCreateView.as_view(), name="notes-list-create"),
    path("notes/<int:pk>/", NoteDetailView.as_view(), name="note-detail"),

    path('categories/', CategoryListCreateView.as_view(), name='categories-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),

    path('tags/', TagListCreateView.as_view(), name='tags-list-create'),
    path('tags/<int:pk>/', TagDetailView.as_view(), name='tag-detail'),
]
