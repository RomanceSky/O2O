from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from ETC.api.serializer import UploadImageSerializer
from ETC.models import UploadedImageModel
""" 
 
class UploadImageViewSet(viewsets.ModelViewSet):
    
    def create(self, request, *args, **kwargs):
        self.serializer_class = UploadImageSerializer
        file = request.data.dict()
        # file['image'] = request.FILES.get('image')
        serial = UploadImageSerializer(data=file)
        if not serial.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
 
        serial.save()
        return Response(serial.data)
 
    def list(self, request, *args, **kwargs):
        self.serializer_class = UploadImageSerializer
        self.queryset = UploadedImageModel.objects.all()
        return super(UploadImageViewSet, self).list(request)
"""
