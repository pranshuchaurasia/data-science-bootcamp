import mysql.connector as connection

mydb = connection.connect(host="localhost", user="root", passwd="")
print(mydb)
cursor = mydb.cursor()

cursor.execute("select student_id, salary from pran.student")

l = []
for i in cursor.fetchall():
    print(i)
    l.append(i)

print(l)
print(type(l[0]))
