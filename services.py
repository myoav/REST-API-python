import datetime
import pymongo
import json
class Services:
    # def __init__(self):
    #     client = pymongo.MongoClient("mongodb+srv://Yoav:Yoav1993@cluster0-pzmee.mongodb.net/test?retryWrites=true&w=majority")
    def insert_new_user(self, jso):
        client = pymongo.MongoClient("mongodb+srv://Yoav:Yoav1993@cluster0-pzmee.mongodb.net/test?retryWrites=true&w=majority")
        db = client.users
        id = jso['ID']
        nickname = jso['Nickname']
        username = jso['Username']
        password = jso['Password']
        create_time = datetime.datetime.now()
        status = jso['Status']
        db.data.insert_one(
            {'_id': id,
             "nickname": nickname,
             "username": username,
             "password": password,
             "create_time" : create_time,
             "status": status}
        )
        if 'Password' in jso:
            del jso['Password']
        jso['create_time'] = create_time
        return jso
