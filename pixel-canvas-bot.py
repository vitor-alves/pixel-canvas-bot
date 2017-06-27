import requests
import simplejson as json

url = "http://pixelcanvas.io/api/me"
headers = {'Content-type': 'application/json', 'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-US,en;q=0.8,pt;q=0.6', 'Connection': 'keep-alive', 'Host':'pixelcanvas.io', 'Origin':'http://pixelcanvas.io', 'Referer':'http://pixelcanvas.io/@-172,-484', 'Save-Data':'on', 'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36'}
rget = requests.get(url, headers=headers)
print(rget.text)

url = "http://pixelcanvas.io/api/pixel"
data = {'x': '-172', 'y': '-484', 'color': '5', 'fingerprint': 'a684e994b234446966da451b5af181b5', 'token': 'null'}
headers = {'Content-type': 'application/json', 'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-US,en;q=0.8,pt;q=0.6', 'Connection': 'keep-alive', 'Host':'pixelcanvas.io', 'Origin':'http://pixelcanvas.io', 'Referer':'http://pixelcanvas.io/@-172,-484', 'Save-Data':'on', 'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36'}
r = requests.post(url, data=json.dumps(data), headers=headers)

print(r.text + "\n")
print(r.headers)
print(json.dumps(data))
