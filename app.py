from flask import Flask,request,jsonify

app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello_world():
   return jsonify({'ID_YOAV': request.json['ID']})




if __name__ == '__main__':
    app.run()
