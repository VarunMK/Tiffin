import json
from flask import Flask, request,Response, jsonify
from flask_cors import CORS,cross_origin
app=Flask(__name__)
CORS(app)


@app.route('/')
def health():
    return 'Server is running'

@app.route('/startContainer',methods=['POST','GET'])
@cross_origin()
def resp():
    if(request.method=='GET'):
        return jsonify({'message':'Success'})
    else:
        data=request.get_json()
        return jsonify(data)

def __init__(self):
    app.run(debug=True)