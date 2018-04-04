from django.shortcuts import render

# Create your views here.
#: 使用Django的REST_framework来写
from .serializer import GoodsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import Goods

#: 使用mixins让代码变得更简洁
from rest_framework import mixins
from rest_framework import generics
#: 分页功能
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets

#:自定义过滤器
from django_filters.rest_framework import DjangoFilterBackend
from .filter import GoodsFilter


#: 配置分页规则
class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "p"
    max_page_size = 1000


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    filter_backends = (DjangoFilterBackend,)
    filter_class = GoodsFilter


class GoodsListView(generics.ListAPIView):
    queryset = Goods.objects.all()[:10]
    serializer_class = GoodsSerializer

    

"""
#: 商品列表
class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Goods.objects.get_queryset().order_by('id')
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination

    #: 过滤
    def get_queryset(self):
        return Goods.objects.filter(shop_price__gt=100)
"""
#class GoodsListView(APIView):
#   def get(self, request, format=None):
#        goods = Goods.objects.all()[:10]
        #: 序列化
#        goods_serializer = GoodsSerializer(goods, many=True)
#        return Response(goods_serializer.data)


