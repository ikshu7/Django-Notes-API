from rest_framework import serializers
from .models import Remainder, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class RemainderSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only = True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset = Category.objects.all(), 
        source = 'category', 
        write_only = True, 
        allow_null = True
        )
    
    class Meta:
        model = Remainder
        fields = ["id", "title", "description", "category", "category_id"]
