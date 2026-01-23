from rest_framework import serializers
from .models import Remainder

class RemainderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remainder
        fields = ["id", "title"]
