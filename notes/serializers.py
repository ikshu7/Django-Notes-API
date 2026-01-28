from rest_framework import serializers
from .models import Notes, Category, Tag

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

        
class NotesSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only = True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset = Category.objects.all(), 
        source = 'category', 
        write_only = True, 
        allow_null = True
        )

    tags = TagSerializer(read_only = True, many = True)
    tag_ids = serializers.PrimaryKeyRelatedField(
        queryset = Tag.objects.all(), 
        many = True, 
        source = 'tags', 
        write_only = True,         
        required = False
        )


    class Meta:
        model = Notes
        fields = [
            'id', 'title', 'content', 
            'created_at', 'updated_at',
            'category', 'category_id',
            'tags', 'tag_ids'
        ]