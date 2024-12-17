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
            'created_at', 'updated_at', 'category_id',
            'youtube', 'spotify'
        ]
        extra_kwargs = {
            'file': {'required': True},
            'cover_image': {'required': False},
        }

class MultiplePDFUploadSerializer(serializers.Serializer):
    files = serializers.ListField(
        child=serializers.FileField(),
        allow_empty=False,
        write_only=True
    )
    cover_image = serializers.ImageField(required=False)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(allow_blank=True, required=False)
    long_description = serializers.CharField(allow_blank=True, required=False)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        write_only=True,
        allow_null=True
    )
    youtube = serializers.URLField(required=False, allow_null=True)
    spotify = serializers.URLField(required=False, allow_null=True)


    # def create(self, validated_data):
    #     files = validated_data.pop('files')
    #     documents = []
    #     for file in files:
    #         document_data = {
    #             'file': file,
    #             **validated_data,
    #         }
    #         documents.append(PDFDocument.objects.create(**document_data))
    #     return documents
    
    def create(self, validated_data):
        files = validated_data.pop('files')  # Extract the list of files
        category = validated_data.pop('category_id', None)  # Extract category_id

        documents = []
        for file in files:
            document_data = {
                'file': file,
                'category_id': category.id if category else None,  # Ensure proper category assignment
                **validated_data
            }
            documents.append(PDFDocument.objects.create(**document_data))
        return documents




# class PDFDocumentSerializer(serializers.ModelSerializer):
#     category = CategorySerializer(read_only=True)
#     # tags = TagSerializer(many=True, read_only=True)
#     created_by = UserSerializer(read_only=True)

#     category_id = serializers.PrimaryKeyRelatedField(
#         queryset=Category.objects.all(),
#         source='category',
#         write_only=True,
#         allow_null=True
#     )

#     class Meta:
#         model = PDFDocument
#         fields = [
#             'id', 'file', 'cover_image', 'title', 'description', 
#             'long_description', 'category', 'tags', 'created_by', 
#             'created_at', 'updated_at', 'category_id', 'tags', 
#             'youtube', 'spotify'  # Add these fields to the serializer
#         ]
#         extra_kwargs = {
#             'file': {'required': True},
#             'cover_image': {'required': False},
#         }

