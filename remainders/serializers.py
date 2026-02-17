from rest_framework import serializers
from .models import Remainder

from main.models import Category
from main.serializers import CategorySerializer


class RemainderSerializer(serializers.ModelSerializer):
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
        model = Remainder
        fields = [
            "id",
            "title",
            "description",
            "remind_at",
            "is_completed",
            "created_at",
            "owner",
            "category",
            "category_id",
        ]
        read_only_fields = ("created_at",)
