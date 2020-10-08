from flask import jsonify
import pymongo
import json
from pymongo import MongoClient
from bson.json_util import dumps, loads

client = pymongo.MongoClient(
    "mongodb+srv://flo:Azerty123@cluster0.ibhol.mongodb.net/blueOrigin?retryWrites=true&w=majority")
db = client.get_database('blueOrigin')


class RocketResource():
    def getAllRockets(self):
        response = json.loads(dumps(db.rocketinventories.find()))
        # print(response)
        return jsonify(response)
    def getRocketById(self, id):
        return jsonify(json.loads(dumps(db.rocketinventories.find_one({"rocketName": id}))))
