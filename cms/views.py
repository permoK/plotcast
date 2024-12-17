# views.py
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

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

    @action(detail=False, methods=['post'], url_path='upload-multiple')
    def upload_multiple(self, request, *args, **kwargs):
        serializer = MultiplePDFUploadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        documents = serializer.save()
        return Response(
            {"documents": [PDFDocumentSerializer(doc).data for doc in documents]},
            status=status.HTTP_201_CREATED
        )


# class PDFDocumentViewSet(viewsets.ModelViewSet):
#     queryset = PDFDocument.objects.all()
#     serializer_class = PDFDocumentSerializer
#     parser_classes = (MultiPartParser, FormParser)

#     def perform_create(self, serializer):
#         # Set the created_by to the default admin user
#         admin_user = User.objects.get(username='peekay')
#         serializer.save(created_by=admin_user)


