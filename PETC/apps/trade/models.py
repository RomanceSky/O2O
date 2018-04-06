from django.db import models

# Create your models here.
from datetime import datetime
from django.contrib.auth import get_user_model
from goods.models import Goods
#from apps.goods.models import Goods


#from users.models import  UserProfile
#import sys
#sys.path.append("../..")
#from apps.goods.models import Goods

User = get_user_model()

"""
***************************************

名称: 购物车
作者:Jun
时间: 2018-03-30

***************************************
"""

class ShoppingCar(models.Model):
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, verbose_name='商品', on_delete=models.CASCADE)
    goods_num = models.IntegerField(default=0, verbose_name='购买数量')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    nums = models.IntegerField(default=0, verbose_name="购买数量")
    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name

    def __str__(self):
         return '%s(%d)'.format(self.goods.name, self.goods_num)

"""
***************************************

名称: 订单
作者:Jun
时间: 2018-03-30

***************************************
"""

class OrderInfo(models.Model):
    ORDER_STATUS = (
        ('success','成功'),
        ('cancel','取消'),
        ('cancel','待支付'),
    )

    PAY_TYPE = (
        ('alipay','支付宝'),
        ('wechat', '微信'),
    )

    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    order_sn = models.CharField(max_length=30, unique=True, verbose_name='订单号')

    trade_no = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name='交易号')
    pay_status = models.CharField(choices=ORDER_STATUS, max_length=10, verbose_name='订单状态')
    post_script = models.CharField(max_length=200, verbose_name='订单留言')
    order_mount = models.FloatField(default=0.0, verbose_name='订单金额')
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name='支付时间')

    #: 用户信息
    address = models.CharField(max_length=100, default='', verbose_name='收货地址')
    signer_name = models.CharField(max_length=20, default='', verbose_name='签收人')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class meta:
         verbose_name = '订单'
         verbose_name_plural = verbose_name
    
    def __str__(self):
        return str(self.order_sn)
"""
***************************************

名称: 订单的商品详情
作者:Jun
时间: 2018-03-30

***************************************
"""

class OrderGoods(models.Model):
    order = models.ForeignKey(OrderInfo, verbose_name='订单信息', on_delete=models.CASCADE)
    goods =  models.IntegerField(default=0, verbose_name='商品数量')
    goods_num = models.IntegerField(default=0, verbose_name='商品数量')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '订单商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order.order_sn)









































