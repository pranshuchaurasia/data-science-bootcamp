import pymongo

client = pymongo.MongoClient("mongodb+srv://<username>:<password>@cluster0.kxavf.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name":"pranshu",
    "email":"pc@gmail.com",
    "surname":"chaurasia"
}
db1 = client['mongotest']
coll=db1['test']
coll.insert_one(d)