#db01.py

#!/usr/bin/python
# encoding: utf-8
import MySQLdb



# 打开数据库连接
db = MySQLdb.connect("www.bleww.com","remoteuser001","SunVK91203","test" ,charset="utf8")
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")
# 使用 fetchone() 方法获取一条数据库。
data = cursor.fetchone()
print ("Database version : %s " % data)

def sel_table001() :

	# SQL 查询语句
	sql = "SELECT * FROM table001 \
		WHERE c_0 > '%d'" % (1)
	try:
		# 执行SQL语句
		cursor.execute(sql)
		# 获取所有记录列表
		results = cursor.fetchall()
		for row in results:
			c_0 = row[0]
			name = row[1]
			# 打印结果
			print ("c_0=%s,name=%s" % (c_0,name ) ) 
	except:
		print ("Error: unable to fecth data")


sel_table001()



# 关闭数据库连接
db.close()

