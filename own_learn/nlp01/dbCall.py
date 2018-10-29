#dbCall.py

import MySQLdb
import sys
import traceback


print("")
print("dbCall.py Start --------------------  ")
print("")

def initDB():
	db = MySQLdb.connect("www.bleww.com","remoteuser001","SunVK91203","test",charset="utf8" )
	return db

# 打开数据库连接
db = initDB()

def show_version(db):
	# 使用cursor()方法获取操作游标
	cursor = db.cursor()
	# 使用execute方法执行SQL语句
	cursor.execute("SELECT VERSION()")
	# 使用 fetchone() 方法获取一条数据库。
	data = cursor.fetchone()
	print ("Database version : %s " % data)

show_version(db)


def sel_Dept_Total_Quantity(db) :

	# SQL 查询语句
	sql = "SELECT * FROM Dept_Total_Quantity "

	try:
		cursor = db.cursor()
		# 执行SQL语句
		cursor.execute(sql)
		# 获取所有记录列表
		results = cursor.fetchall()
		print("")
		print("     Dept_Total_Quantity ")
		print("")
		print("%s %s %s " % ("deptID".ljust(10),"deptName".ljust(10),"Total".rjust(15) ))
		print("")
		for row in results:
			deptID = row[0]
			deptName = row[1]
			TotalMoney = row[2]
			# 打印结果
			print ("%s %s %s" % (str(deptID).ljust(10),deptName.ljust(10), str(TotalMoney).rjust(10) ) ) 
	except Exception:
		traceback.print_exc()
		#traceback.format_exc()
		#print ("Error: %s " % sys._getframe().f_code.co_name )
		#print ("traceback.print_exc():", traceback.print_exc() )
		#print ("traceback.format_exc():\n%s" % traceback.format_exc() )

sel_Dept_Total_Quantity(db)

def sel_Dept_Monthly_Quantity(db) :

	# SQL 查询语句
	sql = "SELECT * FROM Dept_Monthly_Quantity "

	try:
		cursor = db.cursor()
		# 执行SQL语句
		cursor.execute(sql)
		# 获取所有记录列表
		results = cursor.fetchall()
		print("")
		print("     Dept_Monthly_Quantity ")
		print("")
		print("%s %s %s %s" % ("deptID".ljust(10),"deptName".ljust(10),"saleDate".ljust(10),"Total".rjust(15) ))
		print("")
		for row in results:
			deptID = row[0]
			deptName = row[1]
			saleDate = row[2]
			deptTotalMoney = row[3]
			# 打印结果
			print ("%s %s %s %s" % (str(deptID).ljust(10),deptName.ljust(10), saleDate.ljust(10), str(deptTotalMoney).rjust(10) ) ) 
	except:
		traceback.print_exc()

sel_Dept_Monthly_Quantity(db)


def sel_Product_Total_Quantity(db) :

	# SQL 查询语句
	sql = "SELECT * FROM Product_Total_Quantity "

	try:
		cursor = db.cursor()
		# 执行SQL语句
		cursor.execute(sql)
		# 获取所有记录列表
		results = cursor.fetchall()
		print("")
		print("     Product_Total_Quantity ")
		print("")
		print("%s %s %s %s" % ("prodID".ljust(10),"prodName".ljust(25),"totalQuan".ljust(10),"totalMony".rjust(13) ))
		print("")
		for row in results:
			prodID = row[0]
			prodName = row[1]
			totalQuan = row[2]
			totalMony = row[3]
			# 打印结果
			print ("%s %s %s %s" % (str(prodID).ljust(10),str(prodName).ljust(20), str(totalQuan).ljust(10), str(totalMony).rjust(10) ) ) 
	except:
		traceback.print_exc()

sel_Product_Total_Quantity(db)



def sel_Product_Monthly_Quantity(db) :

	# SQL 查询语句
	sql = "SELECT * FROM Product_Monthly_Quantity "

	try:
		cursor = db.cursor()
		# 执行SQL语句
		cursor.execute(sql)
		# 获取所有记录列表
		results = cursor.fetchall()
		print("")
		print("     Product_Monthly_Quantity ")
		print("")
		print("%s %s %s %s" % ("prodID".ljust(10),"prodName".ljust(25),"saleDate".ljust(10),"totalMony".rjust(13) ))
		print("")
		for row in results:
			prodID = row[0]
			prodName = row[1]
			saleDate = row[2]
			totalMony = row[3]
			# 打印结果
			print ("%s %s %s %s" % (str(prodID).ljust(10),str(prodName).ljust(20), str(saleDate).ljust(10), str(totalMony).rjust(10) ) ) 
	except:
		traceback.print_exc()

sel_Product_Monthly_Quantity(db)



def sel_Sale_Monthly_Quantity(db) :

	# SQL 查询语句
	sql = "SELECT * FROM Sale_Monthly_Quantity "

	try:
		cursor = db.cursor()
		# 执行SQL语句
		cursor.execute(sql)
		# 获取所有记录列表
		results = cursor.fetchall()
		print("")
		print("     Sale_Monthly_Quantity ")
		print("")
		print("%s %s %s %s" % ("empID".ljust(10),"empName".ljust(22),"saleDate".ljust(10),"totalMony".rjust(13) ))
		print("")
		for row in results:
			empID = row[0]
			empName = row[1]
			saleDate = row[2]
			totalMony = row[3]
			# 打印结果
			print ("%s %s %s %s" % (str(empID).ljust(10),str(empName).ljust(20), str(saleDate).ljust(10), str(totalMony).rjust(10) ) ) 
	except:
		traceback.print_exc()

sel_Sale_Monthly_Quantity(db)



def sel_Sale_Total_Quantity(db) :

	# SQL 查询语句
	sql = "SELECT * FROM Sale_Total_Quantity "

	try:
		cursor = db.cursor()
		# 执行SQL语句
		cursor.execute(sql)
		# 获取所有记录列表
		results = cursor.fetchall()
		print("")
		print("     Sale_Total_Quantity ")
		print("")
		print("%s %s %s" % ("empID".ljust(10),"empName".ljust(22),"totalMony".rjust(13) ))
		print("")
		for row in results:
			empID = row[0]
			empName = row[1]
			totalMony = row[2]
			# 打印结果
			print ("%s %s %s" % (str(empID).ljust(10),str(empName).ljust(20), str(totalMony).rjust(10) ) ) 
	except:
		traceback.print_exc()

sel_Sale_Total_Quantity(db)

def closeDB(db):
	db.close();

# 关闭数据库连接
db.close()

print("dbCall.py End --------------------  ")
print("")