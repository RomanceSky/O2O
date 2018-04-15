"""PETC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#from django.urls import path, url
from django.urls import path, include

from django.views.static import serve
from PETC.settings import MEDIA_ROOT

#from MXshop.settings import MEDIA_ROOT

import xadmin

#: rest_framework方式实现api
#from rest_framework.documentation import include _docs_urls
from rest_framework.documentation import include_docs_urls

from goods.views import GoodsListView
#:分页最重要的viewsets和router（路由器）来实现商品列表页
from rest_framework.routers import DefaultRouter
from goods.views import GoodsListViewSet
#from PETC.settings import MEDIA_ROOT

#:将创建一个读/写API，来处理我们项目中的用户信息

from ETC.api import views
from ETC.api.views import *
from django.conf.urls import include
from rest_framework import routers
router = DefaultRouter()
router.register(r'goods', GoodsListViewSet)

#router.register(r'categorys', CategoryViewSet, base_name="categorys")

router = routers.DefaultRouter(trailing_slash=True)
#router.register(r'', UploadImageViewSet, base_name='UploadFile')

urlpatterns = [
#    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path(r'^ueditor/',include('DjangoUeditor.urls' )),
    #: 配置上传文件的访问处理函数
    path('media/<path:path>',serve,{'document_root':MEDIA_ROOT}),
  
    #:
    path('docs', include_docs_urls(title='意艺品')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('goods', GoodsListView.as_view(), name="goods-list"),
    path('', include(router.urls)),
 #   path(r'^snippets/$', include('snippets.api.urls', namespace='snippets')),
]
