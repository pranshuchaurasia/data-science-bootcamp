from flask import Flask, request, jsonify
import pymongo

""" To install mongodb properly:
pip uninstall pymongo
pip install pymongo[srv]
"""

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://<username>:<password>@cluster0.sczj6qj.mongodb.net/?retryWrites=true&w=majority")

db = client.test
print(db)
database = client['taskdb']
collection = database["taskcollection"]

@app.route('/insert/mongo', methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        collection.insert_one({name:number})
        return jsonify((str('succesfully inserted')))

if __name__ == '__main__':
    app.run()
# workaround change the port: app.run(port=5001)