import requests

url = "http://v.juhe.cn/laohuangli/d"
txt = requests.post(url)
print("request: %s " % (txt))


myjson = {
  "userAccount": "54321",
  "date": "2016-12-06 10:26:17",
  "ClickTime": 1480991177,
  "jsonInfo": {
    "lon": 121.5612,
    "lat": 31.1832,
    "isGps": 1,
    "netType": "WIFI",
    "addr": "浦东新区长江南路1099弄56号"
  }
}


# sJOSN = '{"userAccount":"54321","date":"2016-12-06 10:26:17","ClickTime": 1480991177,"jsonInfo":{"lon":121.5612,"lat":31.1832,"isGps":1,"netType":"WIFI","addr":"浦东新区长江南路1099弄56号"}}'
# jValue = json2.loads(sJOSN)
# sValue = json2.dumps(jValue)
# print(jValue)
# print(sValue)



# for key in data:
#     print(key + ":" + str(data[key]))