# views.py
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import *

from .models import *

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PDFDocumentViewSet(viewsets.ModelViewSet):
    queryset = PDFDocument.objects.all()
    serializer_class = PDFDocumentSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        # Set the created_by to the default admin user
        admin_user = User.objects.get(username='peekay')
        serializer.save(created_by=admin_user)


