from django.db import models
from main.models import Category, Tag


class Notes(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    category = models.ForeignKey(Category, on_delete = models.SET_NULL, null = True, blank = True)
    tags = models.ManyToManyField(Tag, blank = True)

    def __str__(self):
        return self.title
    