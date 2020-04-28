import datetime
import pymongo
import json


class Services:
    # def __init__(self):
    #     client = pymongo.MongoClient("mongodb+srv://Yoav:Yoav1993@cluster0-pzmee.mongodb.net/test?retryWrites=true&w=majority")
    def insert_new_user(self, jso):
        client = pymongo.MongoClient(
            "mongodb+srv://Yoav:Yoav1993@cluster0-pzmee.mongodb.net/test?retryWrites=true&w=majority")
        db = client.users
        idd = jso['ID']
        nickname = jso['Nickname']
        username = jso['Username']
        password = jso['Password']
        create_time = datetime.datetime.now()
        status = jso['Status']
        db.profiles.insert_one(
            {'_id': idd,
             "nickname": nickname,
             "username": username,
             "password": password,
             "create_time": create_time,
             "status": status}
        )
        # result = db.profiles.create_index([('id', pymongo.ASCENDING)],unique = True)
        jso['create_time'] = create_time

        if 'Password' in jso:
            del jso['Password']
        return jso

    def export_all_users(self):
        client = pymongo.MongoClient(
            "mongodb+srv://Yoav:Yoav1993@cluster0-pzmee.mongodb.net/test?retryWrites=true&w=majority")
        db = client.users
        # for x in db.profiles.find({}, {"password": 0}):
        #     print(x)

        return    list(db.profiles.find({}, {"password": 0}))