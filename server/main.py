import json
import os
import funcs
from flask import Flask, request,Response, jsonify
from flask_cors import CORS,cross_origin
app=Flask(__name__)
CORS(app)

UPLOAD_PATH='./uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_PATH
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

@app.route('/createContainer',methods=['POST','GET'])
@cross_origin()
def createContainer():
    if(request.method=='GET'):
        return jsonify({'message':'Success'})
    else:
        if('file' not in request.files):
            return jsonify({'message':'No file part in the request','status':404})
        file=request.files['file']
        if file.filename=='':
            return jsonify({'message':'No file selected for uploading','status':404})
        if file:
            if(not os.path.isdir(os.path.join(request.files['contName']))):
                os.mkdir(os.path.join(request.files['contName']))
            file.save(os.path.join(request.files['contName'],file.filename))
            funcs.create_cont(os.path.join(request.files['contName'],file.filename))
        else:
            try:
                if(os.path.isdir(os.path.join(request.files['contName']))):
                    funcs.create_cont(os.path.join(request.files['contName'],file.filename),''.join(i.lower() for i in request.files['pyversion'] if not i.isspace()),request.file['contName'])
                else:
                    return jsonify({'message':'An Error has Occured','status':404})
            except:
                return jsonify({'message':'An Error has Occured','status':404})
        return 'Success'

def __init__(self):
    app.run(debug=True)