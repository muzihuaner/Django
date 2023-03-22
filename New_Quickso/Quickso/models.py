from django.db import models
from importlib_resources._common import _


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=120,verbose_name='名称')
    category = models.CharField(max_length=120,verbose_name='类别')
    icon = models.CharField(max_length=64,verbose_name='图标')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "类别"


class Links(models.Model):
    mname = models.CharField(max_length=64,verbose_name='名称')
    url = models.CharField(max_length=120,verbose_name='链接')
    status = models.CharField(max_length=32,verbose_name='状态')
    title = models.CharField(max_length=255,verbose_name='标题')
    category = models.CharField(max_length=120, default="None",verbose_name='类别')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "链接"
