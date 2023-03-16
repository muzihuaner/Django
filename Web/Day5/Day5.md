# Day5笔记

条件语句

```javascript
   if (condition) {

      } else {
    
      }

      if (condition) {

      } else if (condition) {

      } else if (condition) {
    
      } else {
    
      }
```

函数

```javascript
function func(){
}
执行函数
func()
```

**DOM**

文档对象模型 (DOM) 是 HTML 和 XML 文档的编程接口。它提供了对文档的结构化的表述，并定义了一种方式可以使从程序中对该结构进行访问，从而改变文档的结构，样式和内容。DOM 将文档解析为一个由节点和对象（包含属性和方法的对象）组成的结构集合。简言之，它会将 web 页面和脚本或程序语言连接起来。

```javascript
 var Tag = document.getElementById("xxx");
//根据ID获取标签
tag.innerText
//获取标签文本
tag.innerText=xxx
//设置标签文本
var Tag = document.createElement("xx");
//创建标签
tag.innerText=“哈哈哈"
//设置标签内容
Tag.appendChild(xx);
//添加到xx里

```

**事件的绑定**

```javascript
<input type="button" value="单击添加" ondblclick="add()">
    <ul id="city">

    </ul>
    <script>
     function add() {
      var newTag=document.createElement("li")
      newTag.innerText="北京"
      var parentTag=document.getElementById("city")
      parentTag.appendChild(newTag)
     }
    </script>
```


```javascript
 <input type="text" placeholder="请输入内容" id="myinput" />
    <input type="button" value="单击添加" onclick="add()" />
    <ul id="city"></ul>
    <script>
      function add() {
        // 获取输入框内容
        var text = document.getElementById("myinput");
        // 获取用户输入内容
        var newString = text.value;
        // 判断是否为空
        if (newString.length > 0) {
          var newTag = document.createElement("li");
          newTag.innerText = newString;
          var parentTag = document.getElementById("city");
          parentTag.appendChild(newTag);
          //将输入框清空
          text.value = "";
        } else {
          alert("输入框不能为空");
        }
      }
    </script>
```

注意：DOM中还有许多操作

```
DOM可以实现很多功能，但是比较繁琐
页面上的效果一般用jQuery来实现。/vue.js/react.js
```

知识点回顾

* 编码相关

```



字符与二进制的对应关系（编码)：
	- ASCII编码：256种对应关系
	- GB2312,GBK,中文和亚洲的一些国家【中文2字节】
	- unicode，ucs2、ucs4 
	- UTF-8 【中文3字节】
	- Python解释器默认编码：UTF-8

```

 举个栗子

```python
data="中"
res=data.encode('utf-8')
print(res)
data="中"
res=data.encode('gbk')
print(res)

b'\xe4\xb8\xad'
b'\xd6\xd0'
```

* 计算机中的单位

```
1字节=8位
```

* 字符串格式化

```python
v1="我是{}，今年{}岁".format("小欢",23) #推荐使用
v2="我是%s，今年%d岁" %（"小欢",77,)
name="小欢"
age=23
v3=f"我是{name},今年{age}"  #Python3.6以上支持
```

* 数据类型

```
常见数据类型:int,bool,str,list,tuple（元组),dist,set（集合),float,None
	- 转化布尔值为False：空、None、0
	- 可变和不可变划分，可变：list、set、dist
	- 不可哈希 ：list、set、dist
	- 字典的键/集合的元素，必须是可哈希的类型
主要数据类型：
	- str
	  -独有功能：upper/lower/startswith/split/strip、join
	  注意：Str不可变，不会对原数据进行修改，而是生成一个新的数据
	  - 公共功能：len/索引/切片/for循环/判断包含否
	- list
	  -独有功能：append,insert,remove,pop...
	  注意：由于列表是可变的，所以许多功能是对原数据进行操作
	  - 公共功能：len/索引/切片/for循环/判断包含否
	- dict
	 - 独有功能:get/keys/items/values
	 - 公共功能:len/索引/for循环/判断包含否(判断键效率高)

```

* 运算符

```
基本运算符：+-*/...
一般： 1>2 and 3<10
特殊的逻辑运算：(整体结果取决于谁？)
	v1= 99 and 88 #88
	v2=[] or 10 #10
	v3="中国" or [] #[]

```

推导式：

```python
data=[]
for i in range(10)
	data.append(i)

data1=[for i in range(10)]
data2=[for i in range(10) if i<5] #[0,1,2,3,4]
```

* 函数编程

```
函数基本知识
	- 定义
	- 参数 概念：位置传参/关键字传参/参数默认值/动态参数*args,**kwargs
	- 返回值:
		- 函数一旦遇到return就立即返回，后续代码不再执行
		- 函数有返回值返回None
函数进阶： 
	- Python中以函数为作用域。
	- 全局变量和局部变量 规范：全局变量（大写)，局部变量（小写)
	- 在局部变量中可以使用global关键字 ：引用全局变量
内置函数：
	- bin/hex/odc/max/min/divmod/sorted/open
文件操作：
	- 基本操作：打开、操作、关闭，为了防止忘记关闭文件，可以使用with
	- 打开文件模式：
	- r/rb 读 【文件不存在，报错】【文件夹不存在，报错】
	- w/wb 写（清空) 【文件不存在，新建】【文件夹不存在，报错】
	- a/ab 追加 【文件不存在，新建】【文件夹不存在，报错】
注意：os.makedirs/os.path.exsits,是否存在，不存在新建目录。
```

* 模块

```

分类：
	- 自定义模块
		- os.path,导入模块时python内部会去哪个目录寻找
		- 写py文件时，不要与Python内置模块重名
	- 内置模块：time/datetime/json/re/random/os
	- 第三方模块:requests、flask、pandas

查看当前目录下的所有文件：os.listdir/os.walk
时间模块：时间戳、datetime格式、字符串，三种时间格式可以互相转换
JSON模块： 
	- 格式要求：无元组，无单引号。
	- json.dumps序列化时，只能序列化Python常用数据类型
re正则模块：
	- 正则 \d \w
	- 正则 re.search/re.match/re.findall
	- 贪婪匹配（默认)和非贪婪匹配（个数后面加？) 
第三方模块：
	- pip管理工具
	- 源码
	- wheel包
```

* 面相对象

```
面相对象三大特性：
1.封装
2.继承
3.多态

```

* 前端

```
三部分：
	- HTML
	- CSS
	- JavaScript

- HTML标签
	- div/span/a/img/input/form/table/ul...
	- 块级标签：div
	- 行内标签：span
	注意：行内标签设置高度、宽度、内边距、外边距都是无效的
	- form 表单
		- action 地址
		- method 方式
		- submit按钮
		- 内部标签需要设置name属性
- CSS样式
	-布局一定会用到的样式：
		- div+float(脱离文档流，clear:both,clearfix)
		- 高度和宽度
		- 边距
			- 内边距，padding
			- 外边距，margin

```
