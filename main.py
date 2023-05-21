from flask import Flask, request
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
import numpy as np
import math
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

app.config['JSON_AS_ASCII'] = False

### firebase の認証 ###
cred = credentials.Certificate("/home/yuto/workspace/tsumaguro_backend/tumaguro-d5f7e-firebase-adminsdk-pg6j7-a446a1c082.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Headers', 'Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

@app.route('/')
def index():
    return "This is a test."

@app.route('/userInput', methods=["POST"])
def calculate(): #userが入力した緯度、経度と答えの緯度、経度を受け取り点数計算
    data = json.loads(request.get_data())

    user_data = np.array([data['user_latitude'], data['user_longitude']])
    answer_data = np.array([data['answer_latitude'], data['answer_longitude']])

    distance = np.linalg.norm(user_data - answer_data)
    user_point  = 100 * math.exp(-2*distance) #0 ～ 100 の間で点数を表示

    # doc_ref = db.collection('users').document(data['user_id'])
    doc_ref = db.collection('data').document('users')
    doc_ref.set({
       data['user_id']:{ 'score': user_point } #firebase に user_point を送信
    }, merge = True)

    return {
        'score': user_point
    }

@app.route('/userInput/Result', methods=["GET"])
def Ranking(): 
    doc_ref = db.collection('data').document('users') # firebaseを使用
    doc = doc_ref.get().to_dict()
    
    ''' ### doc example ###
    doc = {
        "aaaaa": {"score": 11},
        "aiufuidaoufi": {"score": 100},
        "naninuneno": {"score": 25}
    }
    '''
    # user_pointをソート, 戻り値は、ソートされた{"UserID":score}
    sorted_data = sorted(doc.items(), key=lambda x: x[1]["score"], reverse = True) 

    #new_data = {k: v["score"] for k, v in sorted_data}
    
    sort_score = {}
    for k, v in sorted_data:
        sort_score[k] = v["score"]

    return sort_score

if __name__ == '__main__':
    app.run(port=5011)

    


    






    