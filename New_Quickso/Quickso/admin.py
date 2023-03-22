from django.contrib import admin

# Register your models here.
from .models import *

admin.site.site_title = '快点搜网站管理系统'
admin.site.site_header = '快点搜网站管理系统'

admin.site.register(Category)
admin.site.register(Links)
