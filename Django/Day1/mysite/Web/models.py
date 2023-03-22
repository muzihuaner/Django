from django.db import models

# Create your models here.

"""  部门表 """


class Department(models.Model):
    # id=models.BigAutoField(verbose_name="ID",primary_key=True)
    title = models.CharField(verbose_name='标题', max_length=32)


"""  员工表 """


class UserInfo(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=16)
    password = models.CharField(verbose_name='密码', max_length=64)
    age = models.IntegerField(verbose_name='年龄')
    account = models.DecimalField(verbose_name='账户余额', max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField(verbose_name='入职时间')

#     无约束
#     department_id=models.BigIntegerField(verbose_name='部门ID')
#     1.有约束
#     -to 与哪张表关联
#     -to_field 与这张表哪列关联
#     2.Django 自动
#     -这里写的是depart，但是在生成数据列时会变成depart_id
#     如果部门删除，关联的用户
#     -删除 on_delete=models.CASCADE
#     -设置为空 null=True,blank=True,on_delete=models.SET_NULL
    depart=models.ForeignKey(to="Department",to_field="id",null=True,blank=True,on_delete=models.SET_NULL)
    # 在Django中做约束
    sex_choice=(
        (1,"男"),
        (2,"女"),
    )
    sex=models.SmallIntegerField(varbose_name="性别",choices=sex_choice)