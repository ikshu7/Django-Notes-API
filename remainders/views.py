from rest_framework import generics
from django.db.models import Q
from django.utils.dateparse import parse_date

from .models import Remainder
from .serializers import RemainderSerializer
from .pagination import SmallResultsSetPagination

class RemainderListCreateView(generics.ListCreateAPIView):
    queryset = Remainder.objects.all().order_by("id")
    serializer_class = RemainderSerializer
    pagination_class = SmallResultsSetPagination

    def get_queryset(self):
        remainders = Remainder.objects.all().order_by("id")

        search = self.request.GET.get("search")
        if search:
            remainders = remainders.filter(
                Q(title__icontains=search) |
                Q(description__icontains=search)
            )

        is_completed = self.request.GET.get("is_completed")
        if is_completed in ["true", "false"]:
            remainders = remainders.filter(
                is_completed=(is_completed == "true")
            )

        remind_from = parse_date(self.request.GET.get("remind_from") or "")
        remind_to = parse_date(self.request.GET.get("remind_to") or "")
        if remind_from:
            remainders = remainders.filter(remind_at__date__gte=remind_from)
        if remind_to:
            remainders = remainders.filter(remind_at__date__lte=remind_to)

        created_from = parse_date(self.request.GET.get("created_from") or "")
        created_to = parse_date(self.request.GET.get("created_to") or "")
        if created_from:
            remainders = remainders.filter(created_at__date__gte=created_from)
        if created_to:
            remainders = remainders.filter(created_at__date__lte=created_to)

        ordering = self.request.GET.get("ordering")
        allowed_ordering = {
            "created_at", "-created_at",
            "remind_at", "-remind_at",
            "title", "-title"
        }
        if ordering in allowed_ordering:
            remainders = remainders.order_by(ordering)
        else:
            remainders = remainders.order_by("id")

        return remainders


class RemainderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Remainder.objects.all()
    serializer_class = RemainderSerializer

