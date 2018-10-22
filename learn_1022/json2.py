
import json
import jsonpath
import requests

# url = 'https://www.lagou.com/lbs/getAllCitySearchLabels.json'
url = 'https://api.douban.com/v2/book/1220562'
resp = requests.get(url)
requests.post()
city_json = resp.text

# json字符串转换为python字典对象
city_dict = json.loads(city_json)

# 使用jsonpath匹配
# 获取根节点下的所有name节点的值
names = jsonpath.jsonpath(city_dict, expr='$..name')
print(names)
# 根节点下的message节点的值
message = jsonpath.jsonpath(city_dict, expr='$.message')
print(message)
# # D节点下的前3个
# D = jsonpath.jsonpath(city_dict, expr='$.content.data.allCitySearchLabels.D[0:3]')
# print(D)
# # D节点下的第2个和第4个
# D = jsonpath.jsonpath(city_dict, expr='$.content.data.allCitySearchLabels.D[1,3]')
# print(D)
