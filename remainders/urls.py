from django.urls import path
from .views import (
    RemainderListCreateView,
    RemainderDetailView,
)

urlpatterns = [
    path("remainders/", RemainderListCreateView.as_view(), name="remainders-list-create"),
    path("remainders/<int:pk>/", RemainderDetailView.as_view(), name="remainders-detail"),
]

