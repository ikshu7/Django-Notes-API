from django.urls import path
from .views import (
    TodoListCreateView, 
    TodoDetailView,
    CategoryListCreateView, 
    CategoryDetailView,
)

urlpatterns = [
    path('todo/', TodoListCreateView.as_view(), name='todo-list-create'),
    path('todo/<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),

    path('todo/categories/', CategoryListCreateView.as_view(), name='todo-list-create'),
    path('todo/categories/<int:pk>/', CategoryDetailView.as_view(), name='todo-detail'),
]
