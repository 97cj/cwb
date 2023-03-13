# -*- coding: utf-8 -*-
import http.client, urllib
conn = http.client.HTTPSConnection('api.tianapi.com')  #接口域名
params = urllib.parse.urlencode({'key':'4f5f02f59dfd27ee22a28423f4b203f4'})
headers = {'Content-type':'application/x-www-form-urlencoded'}
conn.request('POST','/saylove/index',params,headers)
res = conn.getresponse()
data = res.read()
print(data.decode('utf-8'))