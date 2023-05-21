from flask import Flask, request,jsonify
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("/home/yuto/workspace/tsumaguro_backend/tumaguro-d5f7e-firebase-adminsdk-pg6j7-a446a1c082.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

doc_ref = db.collection("data").document("users")
doc_ref.set({
    "aaaaa": {"score": 11},
    "aiufuidaoufi": {"score": 100},
    "naninuneno": {"score": 25}
})

doc_ref = db.collection("data").document("users")
doc = doc_ref.get().to_dict() #{"aaaaa": {"score": 11}, "aiufuidaoufi": {"score": 100}, "naninuneno": {"score": 25}}

# key パラメータには、ソートの基準となるキーを指定します。ここでは、ラムダ式(無名関数)を使用して、各要素のインデックス 1 (x[1]) のキー "score" の値をソートの基準としています。
sorted_data = sorted(doc.items(), key=lambda x: x[1]["score"], reverse = True) 

new_data = {k: v["score"] for k, v in sorted_data}

print(new_data)

'''
data_list = []
for item in sorted_data:
    print(item)                         # ('aiufuidaoufi', {'score': 100})
    data_list.append(item)                # ('naninuneno', {'score': 25})
                                         # ('aaaaa', {'score': 11})
print(data_list)

for a, b in data_list:
    print(a, )

datalist = []
for value in doc.values():
    datalist.append(value) # [{"score" : 11}, {"score" : 100}, {"score": 25}]

score = [d["score"] for d in datalist]

#print(sorted(score))

 
#print(datalist)
#print(user_score)


#print(doc)

# print(doc.to_dict()["aaaaa"]["score"])
'''
