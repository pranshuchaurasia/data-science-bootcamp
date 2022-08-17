import mysql.connector as connection
mydb = connection.connect(host="localhost", user="root", passwd="")
print(mydb)
cursor = mydb.cursor()

#cursor.execute("create database pran")
#cursor.execute("show databases")
#cursor.execute("use database pran")
#cursor.execute("create table pran.student (student_id int(10), student_name varchar(20), student_mailid varchar(20), salary int(6))")


q1 = cursor.execute("select * from pran.student")
print(q1)
#print(cursor.fetchall())