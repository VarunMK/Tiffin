import json
import os
import funcs
from flask import Flask, request,Response, jsonify
from flask_cors import CORS,cross_origin
app=Flask(__name__)
CORS(app)

PROJECT_PATH=os.path.join('./projects')
app.config['PROJECT_FOLDER'] = PROJECT_PATH
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
            curr_dir=os.path.join(app.config['PROJECT_FOLDER'],request.args.get('contName'))
            if(not os.path.isdir(os.path.join(curr_dir))):
                os.mkdir(os.path.join(curr_dir))
            file.save(os.path.join(curr_dir,file.filename))
            return 'success'
        else:
            try:
                if(os.path.isdir(os.path.join(request.args.get('contName')))):
                    funcs.create_cont(os.path.join(request.args.get('contName'),file.filename),''.join(i.lower() for i in request.args.get('pyversion') if not i.isspace()),request.args.get('contName'))
                else:
                    return jsonify({'message':'An Error has Occured','status':404})
            except:
                return jsonify({'message':'An Error has Occured','status':404})
        return 'Success'

def __init__(self):
    app.run(debug=True)