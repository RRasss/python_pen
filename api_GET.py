#coding=utf-8
import re
import httplib
import urllib
import socket
import json

headers={"Content-type":"application/x-www-form-urlencoded",
"Accept":"text/plain"
}
'''HTTP GET'''
cc=httplib.HTTPConnection('api.wooyun.org')
cc.request('GET','/bugs/submit')
r=cc.getresponse()
rr=r.read()
ddata=json.loads(rr)
for x in xrange(1,10):
	print ddata[x].values()[8],ddata[x].values()[2],ddata[x].values()[7],ddata[x].values()[5]
