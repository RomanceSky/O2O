# -*- coding: utf-8 -*-

from rest_framework import serializers
from .models import Goods, GoodsCategory

class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        #: 序列化指定字段
        #: 序列化全部字段
        fields = "__all__"

"""
——————————————————————
名称: 商品品牌类别
作者: Jun
时间: 2018-04-04

——————————————————————
"""
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


#class GoodsSerializer(serializers.Serializer):
#    name = serializers.CharField(required=True, max_length=100)
#    click_num = serializers.IntegerField(default=0)
#    goods_front_image = serializers.ImageField()


