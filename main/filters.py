from django.db.models import Q
from django.utils.dateparse import parse_date


def apply_search(queryset, search, fields):
    if search:
        q = Q()
        for field in fields:
            q |= Q(**{f"{field}__icontains": search})
        return queryset.filter(q)
    return queryset


def apply_category_filter(queryset, category_param):
    if category_param:
        if category_param.isdigit():
            return queryset.filter(category_id=int(category_param))
        return queryset.filter(category__name__iexact=category_param)
    return queryset


def apply_date_range(queryset, field, start, end):
    start_date = parse_date(start or "")
    end_date = parse_date(end or "")

    if start_date:
        queryset = queryset.filter(**{f"{field}__date__gte": start_date})
    if end_date:
        queryset = queryset.filter(**{f"{field}__date__lte": end_date})

    return queryset


def apply_ordering(queryset, ordering, allowed_ordering):
    if ordering in allowed_ordering:
        return queryset.order_by(ordering)
    return queryset.order_by("id")
