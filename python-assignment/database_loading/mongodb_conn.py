import pymongo
import newdataloading
import logging as logger
import pandas as pd

client = pymongo.MongoClient("mongodb+srv://<username>:<password>@cluster0.sczj6qj.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
# In MongoDB, a collection is not created until it gets content!
database = client['dress_records']
#collection = database["Dress Attributes"]

df = newdataloading.df
df1 = newdataloading.df1
df.columns =['Dress_ID','29/8/2013','31/8/2013','09-02-2013','09-04-2013','09-06-2013','09-08-2013','09-10-2013','09-12-2013','14/9/2013','16/9/2013','18/9/2013','20/9/2013','22/9/2013','24/9/2013','26/9/2013','28/9/2013','30/9/2013','10-02-2013','10-04-2013','10-06-2013','10-08-2010','10-10-2013','10-12-2013' ]
df = df[1:]

df1_dict = df1.to_dict("records")
 collection.insert_many(df1_dict)

collection1 = database["Dress Sales"]
df_dict = df.to_dict("records")
collection1.insert_many(df_dict)

