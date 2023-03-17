# 员工管理系统

* 使用MYSQL内置工具(命令)
* 创建数据库unicom
* 创建数据表admin:

```
表名：admin
列：
	id,整型,自增,主键
	username,字符串,不为空
	password,字符串,不为空
	mobile,字符串,不为空

```

Python代码实现:

* 添加用户
* 删除用户
* 查看用户
* 更新用户信息

### 创建数据库

```sql
create database unicom DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
use unicom;
create table admin(
    id int auto_increment primary key,
    username varchar(64) not null,
    password char(64) not null,
    mobile char(11) not null
)default charset=utf8;
```


### 使用Python操作数据库

```
pip install pymysql
```

##### 1.创建数据

```python
import pymysql
#1.连接mysql
conn=pymysql.connect(host="127.0.0.1",port=3306,user='root',passwd='lihuan218',charset='utf8',db='unicom')
# 2.发送指令器
cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)

# 3.发送指令
cursor.execute("insert into admin(username,password,mobile) values('小欢','admin','13546796896')")

conn.commit()

# 4.关闭连接
cursor.close()
conn.close()
```

```python
import pymysql


while True:
    user = input("输入用户名:")
    if user.upper()=='Q':
        break
    passwd = input("输入密码:")
    moblie = input("输入手机号:")

# 1.连接mysql
    conn = pymysql.connect(host="127.0.0.1", port=3306, user='root',
                       passwd='lihuan218', charset='utf8', db='unicom')
# 2.发送指令器
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 3.发送指令（千万不要用字符串格式化做SQL的拼接！！！有安全隐患，容易被SQL注入）
# 以下为正确做法
# 方法1：
# sql="insert into admin(username,password,mobile) values(%s,%s,%s)"
# cursor.execute(sql,["小欢","passwd","13546796896"])
# 方法2：
    # sql = "insert into admin(username,password,mobile) values(%(n1)s,%(n2)s,%(n3)s)"
    # cursor.execute(sql, {"n1": "小欢", "n2": "passwd", "n3": "13546796896"})

    sql="insert into admin(username,password,mobile) values(%s,%s,%s)"
    cursor.execute(sql,[user,passwd,moblie])
    conn.commit()

# 4.关闭连接
    cursor.close()
    conn.close()

```

##### 2.查询数据

```python
# 1.连接数据库
import pymysql
conn = pymysql.connect(host="127.0.0.1", port=3306, user='root',
                       passwd='lihuan218', charset='utf8', db='unicom')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)


cursor.execute("select * from admin where id>%s",[2,])
datalist=cursor.fetchall()
for row_dict in datalist:
    print(row_dict)

cursor.close()
conn.close()
```


```python
# 1.连接数据库
import pymysql
conn = pymysql.connect(host="127.0.0.1", port=3306, user='root',
                       passwd='lihuan218', charset='utf8', db='unicom')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)


cursor.execute("select * from admin where id>%s",[2,])
# 获取符合条件的所有数据
# datalist=cursor.fetchall()
# for row_dict in datalist:
#     print(row_dict)
# 获取符合条件的第1个数据
res=cursor.fetchone()
print(res)



cursor.close()
conn.close()
```

##### 3.删除数据

```python
import pymysql
conn = pymysql.connect(host="127.0.0.1", port=3306, user='root',
                       passwd='lihuan218', charset='utf8', db='unicom')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

cursor.execute("delete from admin where id=%s",[3, ])
conn.commit()

cursor.close()
conn.close()
```

##### 4.修改数据

```python
import pymysql
conn = pymysql.connect(host="127.0.0.1", port=3306, user='root',
                       passwd='lihuan218', charset='utf8', db='unicom')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

cursor.execute("update admin set mobile =%s where id=%s",["15546783328",2, ])
conn.commit()

cursor.close()
conn.close()
```
