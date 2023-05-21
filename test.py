from flask import Flask, request,jsonify
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

doc_ref = db.collection('data').document('users')
doc = doc_ref.get().to_dict()
print(doc)
    # user の得点をソートするプログラム
    # 戻り値は、ソート後の{"UserID":score}
sorted_data = sorted(doc.items(), key=lambda x: x[1]["score"], reverse = True) 
print(sorted_data)
    #new_data = {k: v["score"] for k, v in sorted_data}
    
sort_score = {}
for k, v in sorted_data:
    sort_score[k] = v["score"]
print(sort_score)

@app.route('/userInput/Result', methods=["POST"])
def Ranking(): #userID, user_point, Rankingを返す #firebaseを使用
    doc_ref = db.collection('data').document('users')
    doc = doc_ref.get().to_dict()

    # user の得点をソートするプログラム
    # 戻り値は、ソート後の{"UserID":score}
    sorted_data = sorted(doc.items(), key=lambda x: x[1]["score"], reverse = True) 

    #new_data = {k: v["score"] for k, v in sorted_data}
    
    sort_score = {}
    for k, v in sorted_data:
        sort_score[k] = v["score"]
    return sort_score

