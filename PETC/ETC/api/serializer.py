from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ETC.models import UploadedImageModel
 
class UploadImageSerializer(ModelSerializer):
 
    class Meta:
        model = UploadedImageModel
        fields = ('name','note','image','operator','status')
