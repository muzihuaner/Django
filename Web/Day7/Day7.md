# Day7

时间选择插件

https://uxsolutions.github.io/bootstrap-datepicker/

文档

https://bootstrap-datepicker.readthedocs.io/en/latest/

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="static/plugins/bootstrap-3.4.1-dist/css/bootstrap.css">
    <link rel="stylesheet" href="static/plugins/font-awesome-4.7.0/css/font-awesome.css">
    <link rel="stylesheet" href="static/plugins/bootstrap-datepicker-1.9.0-dist/css/bootstrap-datepicker.css">

</head>

<body>
    <div class="container">
        <form class="form-horizontal" style="margin-top: 20px;">
            <div class="row clearfix">
                <div class="col-xs-6">
                    <div class="form-group">
                        <label for="inputEmail3" class="col-sm-2 control-label">电子邮箱</label>
                        <div class="col-sm-10">
                            <input type="email" class="form-control" id="inputEmail3" placeholder="">
                        </div>
                    </div>
                </div>
                <div class="col-xs-6">
                    <div class="form-group">
                        <label for="inputPassword3" class="col-sm-2 control-label">部门</label>
                        <div class="col-sm-10">
                            <select name="" id="" class="form-control">
                                <option value="IT部门">IT</option>
                                <option value="人力资源">HR</option>
                                <option value="管理">OP</option>
                            </select>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row clearfix">
                <div class="col-xs-6">
                    <div class="form-group">
                        <label for="inputPassword3" class="col-sm-2 control-label">密码</label>
                        <div class="col-sm-10">
                            <input type="password" class="form-control" id="inputPassword3" placeholder="Password">
                        </div>
                    </div>
                </div>
                <div class="col-xs-6">
                    <div class="form-group">
                        <label class="col-sm-2 control-label">入职时间</label>
                        <div class="col-sm-10">
                            <input type="text" id="dt" class="form-control">
                        </div>
                  
                    </div>
                </div>
            </div>
            <div class="row clearfix">
                <div class="col-xs-6">
                    <div class="form-group">
                        <div class="col-sm-offset-2 col-sm-10">
                            <button type="submit" class="btn btn-default">登录</button>
                        </div>
                    </div>
                </div>
            </div>
        </form>
    </div>

    <script src="static/js/jquery.min.js"></script>
    <script src="static/plugins/bootstrap-3.4.1-dist/js/bootstrap.js"></script>
    <script src="static/plugins/bootstrap-datepicker-1.9.0-dist/js/bootstrap-datepicker.js"></script>
    <script src="static/plugins/bootstrap-datepicker-1.9.0-dist/locales/bootstrap-datepicker.zh-CN.min.js"></script>
    <script>
        $(function () {
            $('#dt').datepicker({
                format:'yyyy-mm-dd',
                startDate:'0',
                language:'zh-CN',
                autoclose:true
            });
        })
    </script>
</body>

</html>
```

## MYSQL

### 初识网站

* 默认编写的静态效果
* 动态：需要用到Web框架的功能

安装MYSQL

* 5.x
* 8.x

#### MAC下配置Mysql环境变量

**1.启动终端**

**2.进入home目录**

输入cd /Users/YourMacUserName（这里输入你的用户名）

**3.创建.bash_profile文件**

输入touch .bash_profile

如果已经有这个文件，会提示错误，就跳过这一步。

**4.编辑.bash_profile文件**

输入sudo vim .bash_profile，并加入在打开的文本中加入：

export PATH=/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin

export PATH=${PATH}:/usr/local/mysql/bin


**保存，重新打开终端，这时候mysql的命令 *已经可以使用了* **

**（输入mysql -u root -p试一下）。**

### MYSQL语句

登录Mysql

```sql
mysql -u root -p
```

设置密码

```sql
ALTER user 'root'@'localhost' IDENTIFIED BY 'root';--修改密码为roo
```

查看已有数据库

```sql
show databases;
```

退出

```sql
exit;
```

忘记密码怎么办？

https://blog.csdn.net/qixizhuang/article/details/82962121

### MYSQL指令

 MYSQL和我们平时认知的不同概念

| MYSQL  | 认知   |
| ------ | ------ |
| 数据库 | 文件夹 |
| 数据表 | 文件   |

##### 数据库管理

* 查看已有数据库

```sql
show databases;
```

* 创建数据库

```sql
create database 数据库名字
```

```sql
create database 数据库名字 DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
```

举个栗子

```sql
create database mydatabase DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
```

* 删除数据库

```sql
drop database 数据库名字
```

* 进入数据库

```sql
use 数据库名字
```

* 查看数据库里的表

```sql
show tables;
```

##### 数据表管理

* 创建表

```sql
create table 表名称(
	列名称 数据类型,
	列名称 数据类型,
	列名称 数据类型
)default charset=utf8;
```

举个栗子

```sql
create table users (id int,name varchar(16),age int)default charset=utf8;
```

```sql
create table users (
	id int,
	name varchar(16) no null, --不允许为空
	age int null, --允许为空（默认)
)default charset=utf8;
```

```sql
create table users (
	id int,
	name varchar(16),
	age int default 3 --插入数据时，默认值为3
)default charset=utf8;
```

```sql
create table users (
	id int primary key,--主键（不允许为空，也不允许重复)
	name varchar(16),
	age int
)default charset=utf8;
```

主键一般用于表示当前行的编号

```sql
create table users (
	id int auto_increment primary key,--主键（不允许为空，也不允许重复)
	name varchar(16),
	age int
)default charset=utf8;
```

auto_increment 自增

举个栗子

```sql
create table users (
	id int not null auto_increment primary key,
	name varchar(16),
	age int
)default charset=utf8;

```

* 删除表

```sql
drop table 表名称
```

* 展示表格

```sql
desc 表名称
```

举个栗子

```sql
mysql> desc users;
+-------+-------------+------+-----+---------+----------------+
| Field | Type        | Null | Key | Default | Extra          |
+-------+-------------+------+-----+---------+----------------+
| id    | int         | NO   | PRI | NULL    | auto_increment |
| name  | varchar(16) | YES  |     | NULL    |                |
| age   | int         | YES  |     | NULL    |                |
+-------+-------------+------+-----+---------+----------------+
3 rows in set (0.00 sec)
```

##### 数据类型

* tinyint

```
有符号，取值范围 -128~127 (有正有负)【默认】
无符号,取值范围 0~255（只有正)
```

```sql
create table users(
	id int not null auto_increment primary key,
	age tinyint --有符号
)default charset=utf8;
```

```sql
create table users(
	id int not null auto_increment primary key,
	age tinyint unsigned --无符号
)default charset=utf8;
```

* int

带符号范围-2147483648到2147483647，无符号的范围是0到4294967295。 size 默认为 11

* bigint

带符号的范围是-9223372036854775808到9223372036854775807，无符号的范围是0到18446744073709551615。size 默认为 20

* float

带有浮动小数点的小数字。在 size 参数中规定显示最大位数。在 d 参数中规定小数点右侧的最大位数。

* double

带有浮动小数点的大数字。在 size 参数中规显示定最大位数。在 d 参数中规定小数点右侧的最大位数。

* decimal

作为字符串存储的 DOUBLE 类型，允许固定的小数点。在 size 参数中规定显示最大位数。在 d 参数中规定小数点右侧的最大位数。

准确的小数值，m是数字总个数,d是小数后个数,m最大值为65，d最大值为30

```sql
create table L2(
	id int not null auto_increment primary key,
	salary decimal(8,2)
)default charset=utf8;


INSERT INTO L2(salary) VALUES(1.28);
INSERT INTO L2(salary) VALUES(4.285);
INSERT INTO L2(salary) VALUES(422113.28);
INSERT INTO L2(salary) VALUES(42219913.28);#会报错
1	1.28
2	1.28
3	4.29
```

插入数据

```sql
insert into tb2(salary,age) values(10000,23);
```

举个栗子

```sql
insert into tb2(salary,age) values(10000,23);
insert into tb2(salary,age) values(20000,24);
insert into tb2(salary,age) values(20000,24),(30000,38),(40000,40);
```

查看表中的数据

```sql
SELECT * FROM tb2
```

* 字符串
* char （速度快)

保存固定长度的字符串（可包含字母、数字以及特殊字符）。在括号中指定字符串的长度。最多 255 个字符。

```sql
create table L3(
	id int not null auto_increment primary key,
	mobile char(11) --固定11字符存储，就算没有11个字符也会存储11字符
)default charset=utf8;

insert into L3(mobile) values("1234");
insert into L3(mobile) values("12345678910");
```

* varchar （节省空间)

保存可变长度的字符串（可包含字母、数字以及特殊字符）。在括号中指定字符串的最大长度。最多 255 个字符。 **注释：** 如果值的长度大于 255，则被转换为 TEXT 类型。

```sql
create table L3(
	id int not null auto_increment primary key,
	mobile varchar(11) --真实有多长，存储多少字符
)default charset=utf8;
```

* text

存放最大长度为 65,535 个字符的字符串。

```sql
create table L3(
	id int not null auto_increment primary key,
	title varchar(128),
	content text
)default charset=utf8;

一般情况下text用来存储长文本，例如文章、新闻。
```

* mediumtext

存放最大长度为 16,777,215 个字符的字符串。

* longtext

存放最大长度为 4,294,967,295 个字符的字符串。

* datetime

日期和时间的组合。格式：YYYY-MM-DD HH:MM:SS **注释：** 支持的范围是从 '1000-01-01 00:00:00' 到 '9999-12-31 23:59:59'

* data

日期。格式：YYYY-MM-DD **注释：** 支持的范围是从 '1000-01-01' 到 '9999-12-31'

举个栗子：创建用户表

```sql
create table users(
	id int not null auto_increment primary key,
	name varchar(64) not null,
	password char(64) not null,
	email varchar(64) not null,
	age tinyint,
	salary decimal(10,2),
	ctime datetime
)default charset=utf8

INSERT INTO users(name,password,email,age,salary,ctime) VALUES("小欢","password","xiaohuan@qq.com",23,12500.00,"2023-03-17 17:03:00");
```

```
id	name	password	email	age	salary	ctime
1	小欢	password	xiaohuan@qq.com	23	12500.00	2023-03-17 17:03:00
```



平时开发系统时，一般情况下:

* 创建数据库
* 创建数据表

都是需要通过上述命令创建


##### 数据行操作

1.增加

```sql
insert into 表名称(列名称) values(值);
insert into 表名称(列名称,列名称) values(值,值),(值,值),(值,值);
```

2.删除数据

```sql
delete from 表名称;
delete from 表名称 where 条件;
```

举个栗子

删除用户表里id=3的用户

```sql
delete from users where id=3;
delete from users where id=4 and name="xx";
delete from users where id=4 or name="xx";
delete from users where id>4;
delete from users where id!=4;
delete from users where id in (1,5);--把id等于括号里的元素的删除
```

3.修改数据

```sql
update 表名称 set 列=值;
update 表名称 set 列=值,列=值;
update 表名称 set 列=值 where 条件;
update 表名称 set age=age+10 where id>5;
```

4.查询数据

```sql
select * from 表名称; --查询所有数据
select 列名称,列名称 from 表名称;
select 列名称 from 表名称 where 条件;

举个栗子

select * from users;
select id,name from users;
select id,name from users where id>5;
select id,name from users where name="xx" and email="xx@qq.com";

```
