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
