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
]
