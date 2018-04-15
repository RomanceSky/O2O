from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
 
class UploadedImageModel(models.Model):
    STATUS_SIZES = (
        (0, '进行中'),
        (1, '已完成'),
    )
    name = models.CharField('名称', max_length=10)
    create_date = models.DateTimeField("时间", default=timezone.now())
    note = models.CharField('备注', max_length=200, blank=True)
    image = models.ImageField('图片', upload_to='static/images/%Y/%m/%d', blank=False)
    operator = models.CharField('作者', max_length=50, blank=True)
    status = models.IntegerField('状态', default=0, choices=STATUS_SIZES) # 0进行中,1已完成
 
    class Meta:
         db_table = "uploadedimage"
 
    def __str__(self):
         return self.name
