from rest_framework import generics

from .models import Notes
from .serializers import NotesSerializer

from main.pagination import SmallResultsSetPagination
from main.filters import (
    apply_search,
    apply_category_filter,
    apply_date_range,
    apply_ordering,
)


class NotesListCreateView(generics.ListCreateAPIView):
    queryset = Notes.objects.all().order_by("id")
    serializer_class = NotesSerializer
    pagination_class = SmallResultsSetPagination

    def get_queryset(self):
        notes = Notes.objects.all().order_by("id")

        notes = apply_search(
            notes,
            self.request.GET.get("search"),
            fields=("title", "content"),
        )

        notes = apply_category_filter(
            notes,
            self.request.GET.get("category"),
        )

        tags_parameter = self.request.GET.get("tags")
        if tags_parameter:
            tags_list = [x.strip() for x in tags_parameter.split(",") if x.strip()]
            if tags_list:
                if all(tag.isdigit() for tag in tags_list):
                    tag_ids = [int(tag) for tag in tags_list]
                    notes = notes.filter(tags__id__in=tag_ids).distinct()
                else:
                    notes = notes.filter(tags__name__in=tags_list).distinct()

        notes = apply_date_range(
            notes,
            field="created_at",
            start=self.request.GET.get("created_from"),
            end=self.request.GET.get("created_to"),
        )

        notes = apply_ordering(
            notes,
            self.request.GET.get("ordering"),
            allowed_ordering={"created_at", "-created_at", "title", "-title"},
        )

        return notes


class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
