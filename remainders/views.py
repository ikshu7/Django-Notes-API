from rest_framework import generics

from .models import Remainder
from .serializers import RemainderSerializer

from main.pagination import SmallResultsSetPagination
from main.filters import (
    apply_search,
    apply_category_filter,
    apply_date_range,
    apply_ordering,
)

class RemainderListCreateView(generics.ListCreateAPIView):
    serializer_class = RemainderSerializer
    pagination_class = SmallResultsSetPagination

    def get_queryset(self):
        remainders = Remainder.objects.filter(user=self.request.user).order_by("id")

        remainders = apply_search(
            remainders,
            self.request.GET.get("search"),
            fields=("title", "description"),
        )

        remainders = apply_category_filter(
            remainders,
            self.request.GET.get("category"),
        )

        is_completed = self.request.GET.get("is_completed")
        if is_completed in ["true", "false"]:
            remainders = remainders.filter(
                is_completed=(is_completed == "true")
            )

        remainders = apply_date_range(
            remainders,
            field="remind_at",
            start=self.request.GET.get("remind_from"),
            end=self.request.GET.get("remind_to"),
        )

        remainders = apply_date_range(
            remainders,
            field="created_at",
            start=self.request.GET.get("created_from"),
            end=self.request.GET.get("created_to"),
        )

        remainders = apply_ordering(
            remainders,
            self.request.GET.get("ordering"),
            allowed_ordering={
                "created_at", "-created_at",
                "remind_at", "-remind_at",
                "title", "-title",
            },
        )

        return remainders
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RemainderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RemainderSerializer

    def get_queryset(self):
        return Remainder.objects.filter(user=self.request.user)
