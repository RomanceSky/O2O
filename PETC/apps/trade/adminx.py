# -*- coding: utf-8 -*-

import xadmin
from .models import ShoppingCar, OrderInfo, OrderGoods

class ShoppingCarAdmin(object):
    list_display = ["user", "goods", "nums", ]
  

class OrderInfoAdmin(object):
    list_display = ["user", "order_sn", "trade_no", "pay_status", "post_script", "order_mount",
"order_mount", "pay_time", "add_time"]

    class OrderGoodsInline(object):
        model = OrderGoods
        exclude = ['add_time', ]
        extra = 1
        style = 'tab'

    inline = [OrderGoodsInline, ]

xadmin.site.register(ShoppingCar, ShoppingCarAdmin)
xadmin.site.register(OrderInfo, OrderInfoAdmin)


