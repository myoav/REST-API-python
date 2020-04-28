import datetime
import pymongo
import json
class Services:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb+srv://Yoav:Yoav1993@cluster0-pzmee.mongodb.net/test?retryWrites=true&w=majority",connect=False)
        self.db = self.client.users
    def insert_new_user(self, jsonuser):
        # client = pymongo.MongoClient(
        #     "mongodb+srv://Yoav:Yoav1993@cluster0-pzmee.mongodb.net/test?retryWrites=true&w=majority")
        # db = client.users
        # check the argument
        # if len(jsonuser['ID']) > 32 || len():
        #     return "the ID to large"
        create_time = datetime.datetime.now()
        self.db.profiles.insert_one(
            {
             '_id': jsonuser['ID'],
             "Nick name": jsonuser['Nick name'],
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
        # client = pymongo.MongoClient(
        #     "mongodb+srv://Yoav:Yoav1993@cluster0-pzmee.mongodb.net/test?retryWrites=true&w=majority")
        # db = client.users
        # for x in db.profiles.find({}, {"password": 0}):
        #     print(x)

        return list(self.db.profiles.find({}, {"password": 0}))
