from flask import Flask,render_template

app=Flask(__name__)

@app.route("/index")
def index():
    users=["用户0","用户1","用户2"]
    # 找到html文件，读取所有内容
    # 找到html里特殊的占位符，将数据替换，并返回显示在浏览器
    return render_template("index.html",title="学生列表",data_list=users)
if __name__=='__main__':
    app.run()