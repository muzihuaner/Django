import pymysql
conn = pymysql.connect(host="127.0.0.1", port=3306, user='root',
                       passwd='lihuan218', charset='utf8', db='unicom')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

cursor.execute("update admin set mobile =%s where id=%s",["15546783328",2, ])
conn.commit()

cursor.close()
conn.close()