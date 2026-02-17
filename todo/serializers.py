from rest_framework import serializers
from .models import ToDo

from main.models import Category
from main.serializers import CategorySerializer


class TodoSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source="user.username", read_only=True)
    category = CategorySerializer(read_only = True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset = Category.objects.all(), 
        source = 'category', 
        write_only = True, 
        allow_null = True,
        required = False
        )

    class Meta:
        model = ToDo
        fields = [
            "id",
            "title",
            "description",
            "completed",
            "priority",
            "owner",
            "category",
            "category_id",
            "created_at",
            ]
