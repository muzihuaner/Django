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

Get与Post

网络请求是指通过互联网向服务器发送请求以获取数据或执行某些操作的过程。常见的网络请求方法有GET和POST。

GET：
GET是最常用的网络请求方法之一。它通常用于获取数据，例如请求一个网站的HTML文件、图片文件或音频文件等。GET请求是在URL中附加参数发送的，参数在URL的末尾以?键值对形式出现，不同参数之间用&符号分隔。由于参数直接暴露在URL中，因此具有一定的安全风险。

例如，获取一个网站的HTML文件，可以通过如下代码发送GET请求：

```python
import requests
response = requests.get('http://www.example.com')
print(response.content)

```

POST：
POST是另一种常见的网络请求方法，通常用于向服务器提交数据。它与GET请求不同之处在于，POST请求将数据作为请求正文发送。POST请求常用于提交表单数据或上传文件等操作，比如提交注册或登录信息。

例如，提交一个表单数据，可以通过如下代码发送POST请求：

```py
import requests
data = {'username': 'test', 'password': '123456'}
response = requests.post('http://www.example.com/login', data=data)
print(response.content)

```

总的来说，GET请求适合请求数据，而POST请求适合提交数据。但是具体使用方法还需根据具体情况来选择

后端：

```python
@app.route('/get-reg',methods=['GET'])
def get_register():
    # return "注册成功！"
# 1。接收用户Get提交的数据
    print(request.args)
    return "注册成功！"

@app.route('/post-reg',methods=['POST'])
def post_register():
    # return "注册成功！"
# 1。接收用户Post提交的数据
#     print(request.form)
    user=request.form.get('user')
    password=request.form.get('password')
    email=request.form.get('email')
    sex=request.form.get('sex')
    hobby=request.form.get('hobby')
    postion=request.form.get('postion')
    other=request.form.get('other')

    # 将文字写入表格
    df = pd.DataFrame(columns=['用户名','密码', '电子邮箱','性别','爱好','位置','其他'])
    df.loc[len(df)] = [user,password,email,sex,hobby,postion,other]
    timestamp = int(time.time())
    filename = '用户表_{}.csv'.format(timestamp)
    df.to_csv(filename, index=False)
    return "注册成功！"
```

前端：

```html
<form method="post" action="/register">

    <div>
        用户名:<input type="text" name="user" id="user">
    </div>
    <div>
        密码:<input type="password" name="passwd" id="passwd">
    </div>
    <div>
        电子邮箱：<input type="email" name="email" id="email">
    </div>
    <div>
        性别：<input type="radio" name="sex" id="man" value="1">男 <input type="radio" name="sex" id="woman" value="0">女
    </div>
    <div>
        爱好：
        <input type="checkbox" name="hobby" id="coding" value="1">编程
        <input type="checkbox" name="hobby" id="pai" value="2">摄影
        <input type="checkbox" name="hobby" id="fish" value="3">钓鱼
        <input type="checkbox" name="hobby" id="go" value="4">旅行
    </div>
    <div>
        地区：
        <select name="postion" id="postion">
            <option value="山西">山西</option>
            <option value="河南">河南</option>
            <option value="山东">山东</option>
            <option value="河北">河北</option>
        </select>
    </div>
    <div>
        <div>其他信息：</div>
        <textarea name="other" id="info" cols="30" rows="10"></textarea>
    </div>
    <div>
        <input type="submit" value="注册">
        <input type="button" value="登陆">
    </div>
</form>
```
