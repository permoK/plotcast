# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category,  PDFDocument

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_at', 'updated_at']





class PDFDocumentSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    # tags = TagSerializer(many=True, read_only=True)
    created_by = UserSerializer(read_only=True)

    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True,
        allow_null=True
    )

    class Meta:
        model = PDFDocument
        fields = [
            'id', 'file', 'cover_image', 'title', 'description', 
            'long_description', 'category', 'tags', 'created_by', 
            'created_at', 'updated_at', 'category_id', 'tags', 
            'youtube', 'spotify'  # Add these fields to the serializer
        ]
        extra_kwargs = {
            'file': {'required': True},
            'cover_image': {'required': False},
        }

