from flask import Flask, render_template

app = Flask(__name__)


# 可自定义网页目录
# app=Flask(__name__,template_folder="xxx")

# 创建一个网址为/show/info 以及对应的函数关系
# 首页
@app.route("/")
def index():
    return render_template("/index/index.html")

@app.route("/register")
def register():
    return render_template("/index/register.html")

# flask页面
@app.route("/flask")
def flask():
    # return "<h1>Hello,world</h1>"
    # 引入template网页，需要导入 from flask import Flask,render_template
    return render_template("/flask/index.html")


if __name__ == '__main__':
    app.run()
