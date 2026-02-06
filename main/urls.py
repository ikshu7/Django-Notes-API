from django.urls import path
from .views import (
    CategoryListCreateView,
    CategoryDetailView,
    TagListCreateView,
    TagDetailView,
)

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='categories-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),

    path('tags/', TagListCreateView.as_view(), name='tags-list-create'),
    path('tags/<int:pk>/', TagDetailView.as_view(), name='tag-detail'),
]
