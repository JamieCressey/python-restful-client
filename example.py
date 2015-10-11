#!/usr/bin/env python
from RestfulClient.api import ApiClient

api = ApiClient('#key', '#secret', 'http://localhost:5000')

req = api.get('/')
req = api.put('/')
req = api.delete('/')
req = api.post('/')

if req.ok():
	print 'Success!'
else:
	print req.errors()
