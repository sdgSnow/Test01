import json
data = {
    "statusCode": 200,
    "data": {
        "totoal": "5",
        "height": "5.97",
        "weight": "10.30",
        "age": "11"
    },
    "msg": "成功"
}
s = json.dumps(data)
print(s)

s1 = json.loads(s)
print(s1["statusCode"])