from django.urls import path
from .views import TodoListCreateView, TodoDetailView

urlpatterns = [
    path('todo/', TodoListCreateView.as_view(), name='todo-list-create'),
    path('todo/<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
]
