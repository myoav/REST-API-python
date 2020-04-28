from flask import Flask, jsonify, request, abort, make_response
from services import Services

app = Flask(__name__)
services = Services()


@app.route('/')
def hello_world():
    return 'yoyo'


@app.route('/api/users', methods=['POST'])
def new_user():
    return services.insert_new_user(request.json)


@app.route('/api/admin/users', methods=['GET'])
def ecport_user():
    return jsonify({'users': services.export_all_users()})


@app.errorhandler(404)
def notFound(error):
    return make_response("NOT FOUND", 404)


@app.errorhandler(400)
def notFound(error):
    return make_response("INVALID INPUT", 400)


if __name__ == '__main__':
    app.run()
