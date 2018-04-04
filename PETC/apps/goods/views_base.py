# -*- coding: utf-8 -*-

import json
from django.views.generic.base import View
from .models import Goods



"""
————————————————————————————————
名称: 商品列表
作者: Jun
时间: 2018-04-04
描述:
 通过django的view实现商品列表页
         :param request:
         :return:
# 最传统方案，麻烦且add_time序列化会报错
         # for good in goods:
         #     json_dict={}
         #     json_dict["name"]=good.name
         #     json_dict["category"]=good.category.name
         #     json_dict["market_price"]=good.market_price
         #     json_list.append(json_dict)
 
         # 改进方案，但是ImageFieldFile无法进行序列化，报错
         # from django.forms.models import model_to_dict
         # for good in goods:
         #     json_dict=model_to_dict(good)
         #     json_list.append(json_dict)
# 前两个方案使用的代码
         # from django.http import HttpResponse
         # return HttpResponse(json.dumps(json_list),content_type="application/json")
——————————————————————
"""
class GoodsListView(View):
    def get(self, request):
        json_list = []
        goods = Goods.objects.all()[:10]
        from django.core import serializers
        json_data = serializers.serialize("json", goods)
        from django.http import JsonResponse
        return JsonResponse(json_data, safe=False)
 
     
