import pymongo
from flask import Flask,request
from pymongo import MongoClient 
from bson import ObjectId

app = Flask(__name__)

client =MongoClient('mongodb://localhost:27017/') 
db = client['BookStore'] 
collection = db['Book'] 

@app.route('/',methods=["GET"])
def get():
    data = collection.find()
    return data

@app.route('/post',methods=["POST"])
def create():
    collection.insert_one(request.get_json())
    return "data upload"


@app.route('/delete',methods=["DELETE"])
def delete():
    data = request.get_json()
    print(data['id'])
    collection.delete_one({
        "_id":ObjectId(data['id'])
    })
    return "data deleted"

if __name__ == '__main__':
    app.run(host='localhost',port=8000,debug=True)