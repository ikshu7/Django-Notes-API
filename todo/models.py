from django.db import models
from django.contrib.auth.models import User
from main.models import Category


class ToDo(models.Model):
    PRIORITY_NOT_SET = "Not_Set"
    PRIORITY_LOW = "Low"
    PRIORITY_MEDIUM = "Medium"
    PRIORITY_HIGH = "High"

    PRIORITY_CHOICES = [
        (PRIORITY_HIGH, "High"),
        (PRIORITY_MEDIUM, "Medium"),
        (PRIORITY_LOW, "Low"),
        (PRIORITY_NOT_SET, "Not Set"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todo")
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default=PRIORITY_NOT_SET,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey(Category, on_delete = models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
