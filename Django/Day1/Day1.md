# Day1

```python
class Department(models.Model):
    title = models.CharField(verbose_name='标题',max_length=32)
```

> verbose_name='标题'  做一个注释

```python
    account=models.DecimalField(verbose_name='账户余额',max_digits=10,decimal_places=2,default=0)
```

> max_digits=10,decimal_places=2  位数为10，小数点后保留2位

```
1.用户表存储名称? ID?
ID,数据库范式（理论知识）,常见开发都是这样【节省存储开销】
名称，特别大的公司  查询次数非常多，连表操作比较耗时。【加速查找，允许数据冗余】
2.ID 约束
只能是部门表中已存在的ID

```

```python
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

```

