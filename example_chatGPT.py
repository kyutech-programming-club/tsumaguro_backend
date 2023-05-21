'''
my_list = [(1, 2), (3, 4), (5, 6)]

for tuple_item in my_list: #(1,2)を取り出す
    for item in tuple_item: #まず1を取り出して、次に2を取り出す
        print(item)
'''

import json
import time

'''
data = [
    ("John", {"score": 80}),
    ("Alice", {"score": 90}),
    ("Bob", {"score": 75})
]
'''

data2 = {
    "aaaaa": {"score": 11},
    "aiufuidaoufi": {"score": 100},
    "naninuneno": {"score": 25}
}

start = time.time()

sorted_data = sorted(data2.items(), key=lambda x: x[1]["score"], reverse = True) 

#new_data = {k: v["score"] for k, v in sorted_data}

new_data = {}
for k, v in sorted_data:
    new_data[k] = v["score"]

print(json.dumps(new_data))

end = time.time() - start

print(f'{end}秒かかりました!')

a = [("panda", {"score" : 1}), ("kirin",{"score" : 1}), ("neko", {"score" : 1})]

alist = {}
for k, v in a:
    alist[k] = v["score"]

print(alist)


'''
# スコアでソートされたキーと値のペアのリストを作成
sorted_data = sorted(data.items(), key=lambda x: x[1]["score"], reverse=True)

# ソートされたデータから新しいディクショナリを作成
new_data = {}
for key, value in sorted_data:
    new_data[key] = value["score"]

print(new_data)
 

taple = (1,2,3,4,5)
print(taple[1])

for item in taple:
    print(item, end = "\t" )
'''