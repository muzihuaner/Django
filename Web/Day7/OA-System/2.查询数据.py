# 1.连接数据库
import pymysql
conn = pymysql.connect(host="127.0.0.1", port=3306, user='root',
                       passwd='lihuan218', charset='utf8', db='unicom')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)


cursor.execute("select * from admin where id>%s",[2,])
# 获取符合条件的所有数据，得到是列表[字典,字典]。 无数据空列表
# datalist=cursor.fetchall()
# for row_dict in datalist:
#     print(row_dict)
# 获取符合条件的第1个数据,得到的是字典。无数据None
res=cursor.fetchone()
print(res)
cursor.close()
conn.close()