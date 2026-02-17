from rest_framework import serializers
from .models import Notes

from main.models import Category, Tag
from main.serializers import CategorySerializer, TagSerializer

        
class NotesSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source="user.username", read_only=True)

    category = CategorySerializer(read_only = True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset = Category.objects.all(), 
        source = 'category', 
        write_only = True, 
        allow_null = True,
        required = False
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
            'owner',
            'category', 'category_id',
            'tags', 'tag_ids'
        ]
