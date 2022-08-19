import logging
import mysql.connector as connection

logging.basicConfig(filename="mysql_conn.log", level=logging.INFO,
                    format='%(levelname)s %(asctime)s %(name)s  %(message)s')

logging.info("Log after each new run.")

try:
    logging.info("Trying to connect to database.")
    mydb = connection.connect(host="localhost", user="root", passwd="")
    logging.info("Connection to mysql server in localhost successful.")
    logging.info(mydb)
    cursor = mydb.cursor()
    logging.info(cursor)

except Exception as Argument:
    logging.exception(Argument)

try:
    logging.info("Trying to create database dress_records table")
    cursor.execute("create database if not exists dress_records")
    logging.info("Database dress_records creation successful")
except Exception as Argument:
    logging.exception(Argument)


try:
    logging.info("Creating the Table dress_dataset")
    cursor.execute(" create table if not exists dress_records.dress_dataset (Dress_ID INT,`8/2013` INT,`31/8/2013`	INT,`09-02-2013` INT,`09-04-2013` INT,`09-06-2013` INT,`09-08-2013` INT,`09-10-2013` INT,`09-12-2013` INT,`14/9/2013` INT,`16/9/2013` INT,`18/9/2013`  INT,`20/9/2013` INT,`22/9/2013` INT,`24/9/2013` INT,`26/9/2013` INT,`28/9/2013`	 INT,`30/9/2013` INT,`10-02-2013` INT,`10-04-2013` INT,`10-06-2013` INT,`10-10-2013` INT,`10-12-2013` INT)")
    logging.info("Table dress_dataset creation successful")
except Exception as Argument:
    logging.exception(Argument)

try:
    logging.info("Creating the Table attributes_dataset")
    cursor.execute(" create table if not exists dress_records.attributes_dataset  ( Dress_ID int, Style varchar(15), Price VARCHAR(10),Rating FLOAT(5),Size VARCHAR (6),Season VARCHAR(10),NeckLine VARCHAR(10),SleeveLength VARCHAR(10),waiseline VARCHAR(10),Material VARCHAR(10),FabricType VARCHAR(10),Decoration VARCHAR(10),Pattern VARCHAR(10),Type VARCHAR(10),Recommendation INT(1))")
    logging.info("Table attributes_dataset creation successful")
except Exception as Argument:
    logging.exception(Argument)