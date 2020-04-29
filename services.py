import datetime
import pymongo
import json
from flask import abort


class Services:
    def __init__(self):
        self.client = pymongo.MongoClient(
            "mongodb+srv://Yoav:Rest2020@cluster0-pzmee.mongodb.net/test?retryWrites=true&w=majority", connect=False)
        self.db = self.client.users

    def insert_new_user(self, jsonuser):
        # check the argument
        if len(jsonuser['ID']) > 32 | len(jsonuser['Nickname']) > 11 | len(jsonuser['Username']) > 50 | len(
                jsonuser['Password']) > 200 | jsonuser['Status'] > 255:
            abort(400)
        create_time = datetime.datetime.now()
        x = list(self.db.profiles.find({'_id': jsonuser['ID']}))
        if x:
            abort(400)
        self.db.profiles.insert_one(
            {
                '_id': jsonuser['ID'],
                "Nickname": jsonuser['Nickname'],
                "User name": jsonuser['User name'],
                "password": jsonuser['Password'],
                "Create time": create_time,
                "Status": jsonuser['Status']
            }
        )
        jsonuser['create_time'] = create_time
        if 'Password' in jsonuser:
            del jsonuser['Password']
        return jsonuser

    def export_all_users(self):
        return list(self.db.profiles.find({}, {"password": 0}))
