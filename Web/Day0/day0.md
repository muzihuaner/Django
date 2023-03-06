# 前端开发

```
-前端开发 ：三件套 html,css,javascript
- Web框架：接受请求并处理
- Mysql数据库：存储数据
```

快速上手：基于flask web框架

深入学习：基于Django框架

## 1.快速开发网站

```
pip install flask
```

一个栗子：

```python
from flask import Flask

app=Flask(__name__)

# 创建一个网址为/show/info 以及对应的函数关系
@app.route("/show/info")
def index():
    return "Hello,world"

if __name__ =='__main__':
        app.run()
```

列表

```html
<ul>
    <li>中国移动</li>
    <li>中国电信</li>
    <li>中国联通</li>
</ul>
<ol>
    <li>中国移动</li>
    <li>中国电信</li>
    <li>中国联通</li>
</ol>
```

表格

```html
<table border="1">
    <thead>
    <tr>
        <th>姓名</th>
        <th>年龄</th>
        <th>性别</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>xiaohuan0</td>
        <td>23</td>
        <td>男</td>
    </tr>
    <tr>
        <td>xiaohuan1</td>
        <td>23</td>
        <td>男</td>
    </tr>
    <tr>
        <td>xiaohuan2</td>
        <td>23</td>
        <td>男</td>
    </tr>

    </tbody>

</table>
```

其他:

```html

用户名：
<input type="text" name="" id="user">
密码：
<input type="password" name="" id="passwd">
上传：
<input type="file" name="上传" id="">

单选框：
性别：
<input type="radio" name="sex" id="man">男
<input type="radio" name="sex" id="woman">女
复选框:
<input type="checkbox" name="" id="">A
<input type="checkbox" name="" id="">B
<input type="checkbox" name="" id="">C
按钮：
<input type="button" value="提交1">
提交按钮
<input type="submit" value="提交2">
下拉框：

<select>
    <option value="北京">北京</option>
    <option value="上海">上海</option>
    <option value="深圳">深圳</option>
</select>
多选下拉框：
<select multiple>
    <option value="北京">北京</option>
    <option value="上海">上海</option>
    <option value="深圳">深圳</option>
</select>

多行文本:
<textarea name="" id="" cols="30" rows="10">

</textarea>
```

网络请求：
