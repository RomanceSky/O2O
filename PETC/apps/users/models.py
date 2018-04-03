# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
#: 重写User类，覆盖Django内置的User表
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime

"""
**********************************

名称: 自定义的用户表
作者: Jun
时间: 2018-03-30

**********************************
"""

class UserProfile(AbstractUser):
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    gender=models.CharField(max_length=6,choices=(('male','男'),('female','女')),default='male')
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱")

    #: 指定模型
    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

"""
**********************************

名称: 短信验证码
作者: Jun
时间: 2018-03-30

**********************************
"""

class VerifyCode(models.Model):
    code = models.CharField(max_length=10, verbose_name="验证码")
    mobile = models.CharField(max_length=11, verbose_name="电话")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    #: 指定模型
    class meta:
        verbose_name = "短信验证码"
        verbose_name_pural = verbose_name

    def __str__(self):
        return self.code







