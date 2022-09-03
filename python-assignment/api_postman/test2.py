from flask import Flask, request, jsonify
import mysql.connector as connection

mydb = connection.connect(host="localhost", user="root", passwd="")
app = Flask(__name__)
print(mydb)
cursor = mydb.cursor()

cursor.execute("create database IF NOT exists tasksql")
cursor.execute("create table IF NOT exists tasksql.mysqltable(name varchar(30),number int)")


# mydb.commit()

@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        cursor.execute("insert into tasksql.mysqltable values(%s, %s)", (name, number))
        mydb.commit()
        return jsonify((str('succesfullt inserted')))


@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        get_name = request.json['get_name']
        cursor.execute("update tasksql.mysqltable set number = number + 500 where name = %s", (get_name,))
        mydb.commit()
        return jsonify((str('Updated successfully')))

@app.route('/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        name_del = request.json['name_del']
        cursor.execute("delete from tasksql.mysqltable  where name = %s", (name_del,))
        mydb.commit()
        return jsonify((str('successfully deleted')))

@app.route('/fetch', methods=['POST'])
def fetch_data():
    l=[]
    cursor.execute("select * from tasksql.mysqltable")
    for i cursor.fetchall():
        l.append(i)
    return jsonify((str('l')))
if __name__ == '__main__':
    app.run()
