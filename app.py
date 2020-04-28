from flask import Flask,jsonify,request
from services import Services
app = Flask(__name__)
services = Services()


@app.route('/')
def hello_world():
    return 'yoyo'

@app.route('/api/users', methods=['POST'])
def new_user():
    return  services.insert_new_user(request.json)
    # return jsonify({'my data ':services.insert_new_user(request.json)})
@app.route('/api/admin/users', methods=['GET'])
def ecport_user():
    return  jsonify({'users':services.export_all_users()})

if __name__ == '__main__':
    app.run()
