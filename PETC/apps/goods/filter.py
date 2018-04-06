# -*- coding:utf-8 -*-
import django_filters
from .models import Goods

class GoodsFilter(django_filters.rest_framework.FilterSet):
    #: 商品过滤器
    price_min = django_filters.NumberFilter(name='shop_price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(name='shop_price', lookup_expr='lte')
    #: 模糊查询,其中'contains'代表区分大小写，'icontains'代表不区分大小写
    name = django_filters.CharFilter(name='name', lookup_expr='icontains')
    class Meta:
        models = Goods
        fields = ['price_min', 'price_max', 'name']
        #fileds={'price_min', 'price_max', 'name'}




