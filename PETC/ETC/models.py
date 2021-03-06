from django.db import models

from django.utils import timezone

# Create your models here.
class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
)
#    first_name = models.CharField(max_length=30)
#    last_name = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    
    def __str__(self):
        return self.name





class Musician(models.Model):
    fisrt_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
#:  乐器 
"""
——————————————————————————
相册


——————————————————————————
"""
class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

"""
——————————————————————————
关系：一对一、一对多、多对多
如果汽车模型有厂商
一个辆汽车只有一个制造商
一个制造商可以生产多辆汽车
多对一的关系
——————————————————————————

"""
class Manufacturer(models.Model):
    pass

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
"""
——————————————————————————
多对多的关系
一个品种包含多个披萨
一个披萨可以包含多个品种
——————————————————————————
"""
class Topping(models.Model):
    pass

class Pizza(models.Model):
    toppings = models.ManyToManyField(Topping)

"""
——————————————————————————
Extra fields on many-to-many relationships
当需要将数据关联两个数据模型时
音乐家
——————————————————————————
"""
class Group(models.Model):
    name = models.CharField(max_length=128)
    members  = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason =  models.CharField(max_length=64)




#: 实现图片上传
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























