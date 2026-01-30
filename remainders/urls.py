from django.urls import path
from .views import (
    RemainderListCreateView,
    RemainderDetailView,
    CategoryListCreateView,
    CategoryDetailView,
)

urlpatterns = [
    path("remainders/", RemainderListCreateView.as_view(), name="remainders-list-create"),
    path("remainders/<int:pk>/", RemainderDetailView.as_view(), name="remainders-detail"),

    path('remainders/categories/', CategoryListCreateView.as_view(), name='categories-list-create'),
    path('remainders/categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
]
