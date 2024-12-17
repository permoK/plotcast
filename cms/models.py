# pdf_documents/models.py
from django.db import models
from django.contrib.auth.models import User

from django.contrib.postgres.fields import ArrayField
from django.db.models.functions import TruncHour

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class PDFDocument(models.Model):
    file = models.FileField(upload_to='documents')
    cover_image = models.ImageField(upload_to='cover_image')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    long_description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='documents')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_documents', blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)  # Add field for YouTube link
    spotify = models.URLField(blank=True, null=True)  # Add field for Spotify link
    # tags = ArrayField(
    #         models.CharField(max_length=100),
    #         blank = True,
    #         )
    tags = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

