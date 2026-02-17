from django.db import models
from django.contrib.auth.models import User
from main.models import Category


class Remainder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="remainders")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    remind_at = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey(Category, on_delete = models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
