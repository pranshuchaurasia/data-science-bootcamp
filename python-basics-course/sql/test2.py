import mysql.connector as connection
mydb = connection.connect(host="localhost", user="root", passwd="alien008")
print(mydb)
cursor = mydb.cursor()

cursor.execute("insert into pran.student values(101,'rohan','rohan@gmail.com',1000)")
mydb.commit()
cursor.execute("select * from pran.student")
for i in cursor.fetchall():
    print(i)