from django.db import models

# Create your models here.
from datetime import datetime
#from goods.models import Goods
from goods.models import Goods

from django.contrib.auth import get_user_model
User = get_user_model()

"""
***************************************

名称: 用户收藏
作者:Jun
时间: 2018-03-31

***************************************
"""

class UserFav(models.Model):
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, verbose_name='商品', on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name

#    def __str__(self):
 #       return self.user.name

"""
***************************************

名称: 用户留言
作者:Jun
时间: 2018-03-31

***************************************
"""

class UserLeavingMessage(models.Model):
    MESSAGE_CHOICE=(
        (1,'留言'),
        (2,'投诉'),
        (3,'询问'),
        (4,'售后'),
        (5,'求购'),
    )

    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    message_type = models.IntegerField(choices=MESSAGE_CHOICE, verbose_name='留言类型',
help_text='留言类型:1(留言),2(投诉),3(询问),4(售后),5(求购)')
    subject=models.CharField(max_length=100, default='',verbose_name='主题')
    message=models.TextField(default='',verbose_name='留言内容',help_text='留言内容')
    file = models.FileField(verbose_name='上传的文件', help_text='上传的文件')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户留言'
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.subject

"""
***************************************

名称: 用户收货地址
作者:Jun
时间: 2018-03-31

***************************************
"""


class UserAddress(models.Model):
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    district = models.CharField(max_length=100, default='', verbose_name='区域')
    address = models.CharField(max_length=100, default='', verbose_name='详细地址')
    signer_name = models.CharField(max_length=100, default='', verbose_name='签收人')
    signer_mobile = models.CharField(max_length=11, default='', verbose_name='电话')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '收货地址'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.address








































































