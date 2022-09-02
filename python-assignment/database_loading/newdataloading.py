import mysql_conn
import logging as logger
import pandas as pd


try:
    if mysql_conn.mydb.is_connected():
        logger.info("The module my-sql connection in data-loading python file is working perfectly.")
except Exception as Argument:
    logger.error(Argument)
    logger.exception(Argument)
    logger.warning(Argument)


data = pd.read_excel(r'C:\Users\Pranshu Chaurasia\Desktop\data-science-bootcamp\data-science-bootcamp\python-assignment\dataset\Dress Sales.xlsx')
data.to_csv('C:\\Users\\Pranshu Chaurasia\\Desktop\\data-science-bootcamp\\data-science-bootcamp\\python-assignment\\dataset\\Dress Sales.csv',index=False)
data1=data = pd.read_csv(r'C:\Users\Pranshu Chaurasia\Desktop\data-science-bootcamp\data-science-bootcamp\python-assignment\dataset\Dress Sales.csv',header=None)

df = pd.DataFrame(data1)

sql = "INSERT INTO dress_records.dress_dataset values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
for j in range (df.shape[0]):
    if j == 0:
        pass
    else:
        temp_dict= dict(df.iloc[j,:])
        temp_values=temp_dict.values()
        temp_tup=tuple(temp_values)
        l=[]
        x=len(temp_tup)
        for i in range (x):
            if(i==0):
                l.append(int(temp_tup[i]))
            else:
                if(type(temp_tup[i])==type(3.0) or temp_tup[i] =='Orders' or temp_tup[i] =='Removed' or temp_tup[i] =='removed' ):
                    l.append(0.0)
                else:
                    l.append(int(float(temp_tup[i])))

        tup_new=tuple(l)
        mysql_conn.cursor.execute(sql,tup_new)
        mysql_conn.mydb.commit()

cursor1 = mysql_conn.mydb.cursor()
data2 = pd.read_excel(r'C:\Users\Pranshu Chaurasia\Desktop\data-science-bootcamp\data-science-bootcamp\python-assignment\dataset\Attribute DataSet.xlsx')
data2.to_csv('C:\\Users\\Pranshu Chaurasia\\Desktop\\data-science-bootcamp\\data-science-bootcamp\\python-assignment\\dataset\\Attribute DataSet.csv',index=False)
data3=data = pd.read_csv(r'C:\Users\Pranshu Chaurasia\Desktop\data-science-bootcamp\data-science-bootcamp\python-assignment\dataset\Attribute DataSet.csv')
df = pd.DataFrame(data3)
#df.isnull().sum()
df=df.fillna(value='Not available')
df.isnull().sum()
sql = "INSERT INTO dress_records.attributes_dataset values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
for j in range (df.shape[0]):
        temp_dict= dict(df.iloc[j,:])
        temp_values=temp_dict.values()
        temp_tup=tuple(temp_values)
        l=[]
        x=len(temp_tup)
        for i in range (x):
            if(i==0):
                l.append(int(temp_tup[i]))
            elif(i==3):
                l.append(float(temp_tup[i]))
            elif(i==13):
                l.append(int(temp_tup[i]))
            else:
                l.append(str(temp_tup[i]))
        tup_new=tuple(l)
        cursor1.execute(sql,tup_new)
        mysql_conn.mydb.commit()

