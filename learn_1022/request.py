import http.client

#简单的GET请求
# url = 'https://www.lagou.com/lbs/getAllCitySearchLabels.json'
# con = http.client.HTTPConnection(url)
con = http.client.HTTPConnection('www.baidu.com')
con.request("GET", "/index.html",'',{})
resu = con.getresponse()
print("status = %s " % str(resu.status))  #打印读取到的数据
print("reason = %s " % str(resu.reason))  #打印读取到的数据
print("info() = %s " % str(resu.info()))  #打印读取到的数据

#打印读取的数据
print ("读取结果为： %s " % str(resu.read()))

#测试一个无效的请求
inCon = http.client.HTTPConnection('www.baidu.com')
inCon.request('GET', 'None.html')
resu2 = inCon.getresponse()
print("status = %s" % str(resu2.status))
print("msg = %s" % str(resu2.msg))