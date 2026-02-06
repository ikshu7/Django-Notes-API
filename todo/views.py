from rest_framework import generics
from django.db.models import Case, When, IntegerField

from .models import ToDo, Category
from .serializers import TodoSerializer, CategorySerializer
from .pagination import SmallResultsSetPagination
from main.filters import (
    apply_search,
    apply_category_filter,
    apply_date_range,
    apply_ordering,
)


class TodoListCreateView(generics.ListCreateAPIView):
    queryset = ToDo.objects.all().order_by("id")
    serializer_class = TodoSerializer
    pagination_class = SmallResultsSetPagination

    def get_queryset(self):
        todos = ToDo.objects.all().order_by("id")

        todos = apply_search(
            todos,
            self.request.GET.get("search"),
            fields=("title", "description"),
        )

        todos = apply_category_filter(
            todos,
            self.request.GET.get("category"),
        )

        completed = self.request.GET.get("completed")
        if completed in ["true", "false"]:
            todos = todos.filter(completed=(completed == "true"))

            if completed == "true":
                todos = todos.annotate(
                    priority_order=Case(
                        When(priority=ToDo.PRIORITY_HIGH, then=1),
                        When(priority=ToDo.PRIORITY_MEDIUM, then=2),
                        When(priority=ToDo.PRIORITY_LOW, then=3),
                        When(priority=ToDo.PRIORITY_NOT_SET, then=4),
                        output_field=IntegerField(),
                    )
                ).order_by("priority_order", "-created_at")

        todos = apply_date_range(
            todos,
            field="created_at",
            start=self.request.GET.get("created_from"),
            end=self.request.GET.get("created_to"),
        )

        todos = apply_ordering(
            todos,
            self.request.GET.get("ordering"),
            allowed_ordering={
                "created_at", "-created_at",
                "title", "-title",
                "priority", "-priority",
            },
        )

        return todos



class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = TodoSerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    