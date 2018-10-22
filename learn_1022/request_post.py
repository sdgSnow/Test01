import http.client,urllib.parse
# http://docs.python-requests.org/zh_CN/latest/user/quickstart.html
pararms = urllib.parse.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
conn = http.client.HTTPConnection("bugs.python.org")
conn.request('POST', '', pararms, headers)
response = conn.getresponse()
print(response.status, response.reason)
data = response.read()
print(data)

conn.close()