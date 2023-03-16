## jQuery

jQuery 是一个 JavaScript 库。

jQuery 极大地简化了 JavaScript 编程。

* 基于jQuery，自己开发一个功能。
* 现成的工具 依赖jQuery，例如BootStrap动态效果

## 快速上手

* 下载jQuery

https://cdnjs.quickso.cn/ajax/libs/jquery/3.6.4/jquery.min.js

* 引入jQuery

```html
 <script src="https://cdnjs.quickso.cn/ajax/libs/jquery/3.6.4/jquery.min.js"></script>
```

#### 寻找标签(直接寻找)

* ID选择器

```html
<h1 id="txt">中国联通</h1>

    <script>
      // 利用jQuery实现功能
      //找到id为txt的tag并修改文字
      $("#txt").text("中国移动");
  
    </script>
```

* 类选择器

```html
 <h1 class="c1">中国联通</h1>
$(".c1").text("中国电信");
```

* 标签选择器

```
  $("h1")
```

* 层级选择器

```
 $(".nav ul li a")
```

* 多选择器

```
  $("#c1,.c2,li")
```

* 属性选择器

```
$("input[name='id0']");
```

#### 间接寻找

```html
<div>
    <div>bj</div>
    <div id="c1">sh</div>
    <div>cq</div>
    <div>gz</div>
</div>

      $("#c1").prev() //bj上一个
      $("#c1") //sh
      $("#c1").next() //cq 下一个
      $("#c1").next().next()  //gz 下下个

      $("#c1").siblings() //bj,cq,gz  找到所有兄弟
```

* 找父子

```html
 <div>
      <div>
        <div>bj</div>
        <div id="c1">
          <div>1</div>
          <div class="p10">2</div>
          <div>3</div>
        </div>
        <div>cq</div>
        <div>gz</div>
      </div>

      <div>
        <div>sx</div>
        <div>shx</div>
        <div>hb</div>
        <div>sd</div>
      </div>
    </div>


$("#c1").parent(); //父亲
      $("#c1").parent().parent(); //爷爷
      $("#c1").children(); //所有的儿子
      $("#c1").children(".p10"); //所有儿子中寻找class为p10的标签
      $("#c1").find(".p10"); //在所有子孙中寻找
```

#### 菜单切换

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <style>
      .menu {
        width: 200px;
        height: 800px;
        border: 1px solid red;
      }
      .menu .header {
        background-color: gold;
        padding: 10px 5px;
        border-bottom: 1px dotted #dddddd;
        cursor: pointer;
        /* cursor CSS 属性设置光标的类型（如果有），在鼠标指针悬停在元素上时显示相应样式。 */
      }
      .menu .content a {
        display: block;
        padding: 5px 5px;
        text-decoration: none;
        color: black;
        border-bottom: 1px dotted #dddddd;
      }
      .hide {
        display: none;
      }
    </style>
    <script src="https://cdnjs.quickso.cn/ajax/libs/jquery/3.6.4/jquery.min.js"></script>
  </head>
  <body>
    <div class="menu">
      <div class="item">
        <div class="header" onclick="clickMe(this)">免费服务</div>
        <div class="content hide">
          <a href="">免费CDN</a>
          <a href="">免费域名</a>
          <a href="">免费服务器</a>
          <a href="">免费模版</a>
        </div>
      </div>
      <div class="item">
        <div class="header" onclick="clickMe(this)">付费服务</div>
        <div class="content hide">
          <a href="">CDN</a>
          <a href="">域名</a>
          <a href="">服务器</a>
          <a href="">模版</a>
        </div>
      </div>
    </div>
    <script>
      function clickMe(self) {
        // $(self) ->当前单击的标签
        // 判断有没有 .hasClass(）
        // 删除样式 $(self).next().removeClass()
        // 添加 .addClass(）
        var hasHide = $(self).next().hasClass("hide");
        if (hasHide) {
          $(self).next().removeClass("hide");
        } else {
          $(self).next().addClass("hide");
        }
      }
    </script>
  </body>
</html>

```

#### 值的操作

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <script src="https://cdnjs.quickso.cn/ajax/libs/jquery/3.6.4/jquery.min.js"></script>
  </head>
  <body>
    <div class="c1">内容</div>
    <input type="text" id="c2"/>
    <script>
      $("#c1").text(); //获取文本内容
      $("#c1").text("休息"); //设置文本内容
    </script>

    <input type="text" id="c2" />
    <script>
      $("#c2").val(); //获取用户输入的值
      $("#c2").val("设置值"); // 设置值
    </script>
  </body>
</html>

```

#### 动态创建数据

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <script src="https://cdnjs.quickso.cn/ajax/libs/jquery/3.6.4/jquery.min.js"></script>
  </head>
  <body>
    <input type="text" id="txtUser" placeholder="用户名" />
    <input type="email" id="txtEmail" placeholder="邮箱" />
    <input type="button" value="提交" onclick="getInfo()" />

    <ul id="view">
      <li>Info</li>
    </ul>

    <script>
      function getInfo() {
        //获取用户输入内容
        var userName = $("#txtUser").val();
        var userEmail = $("#txtEmail").val();
        var DataString = userName + "-" + userEmail;
        // 创建li，写入内容
        var newLi = $("<li>").text(DataString);
        $("#view").append(newLi);
      }
    </script>
  </body>
</html>

```

### 事件

```html
<body>
    <ul>
        <li>baidu</li>
        <li>google</li>
        <li>sougou</li>
    </ul>
    <script>
        $("li").click(function () {
            // 当单击li标签时，会执行函数。
            // $(this) 当前你点击的是哪个标签。
            var text=$(this).text();
            console.log(text)
        })
    
    </script>
</body>
```

在jQuery中可以删除某个标签

```
$(this).remove()
```

当页面框架加载完成之后执行的代码:

```html
  <script>
      $(function () {
        //当页面框架加载完成之后执行
        $("li").click(function () {
          // 当单击li标签时，会执行函数。
          // $(this) 当前你点击的是哪个标签。
          var text = $(this).text();
          console.log(text);
          $(this).remove();
        });
      });
    </script>
```

#### 表格操作

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script src="https://cdnjs.quickso.cn/ajax/libs/jquery/3.6.4/jquery.min.js"></script>
</head>
<body>
    <table border="1">
        <thead>
            <tr>
                <td>ID</td>
                <td>Name</td>
                <td>Do</td>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>1</td>
                <td>xiaohuan</td>
                <td>
                    <input type="button" value="Delete" class="Delete">
                </td>
            </tr>
            <tr>
                <td>1</td>
                <td>xiaohuan</td>
                <td>
                    <input type="button" value="Delete" class="Delete">
                </td>
            </tr>
            <tr>
                <td>1</td>
                <td>xiaohuan</td>
                <td>
                    <input type="button" value="Delete" class="Delete">
                </td>
            </tr>
        </tbody>
    </table>
    <script>
        $(function(){
            $(".Delete").click(function () {
                // 删除当前行的数据
                $(this).parent().parent().remove()
            })
        })
    
    </script>
</body>
</html>
```
