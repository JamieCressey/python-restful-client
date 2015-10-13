from RestfulClient import __version__
try:
	import json
except ImportError:
	try:
		import simplejson as json
	except ImportError:
		from django.utils import simplejson as json

class ApiClient(object):
	"""
	A client for accessing a RESTful API
	"""
	def __init__(self, api_key, api_secret, api_uri):
		"""
		Create a RESTful API client.
		"""
		self.api_uri	= api_uri
		self.api_key	= api_key
		self.api_secret = api_secret

	def version(self):
		return __version__

	def set_headers(self, nonce = None):
		from base64 import b64encode
		from hashlib import sha256
		from platform import platform, python_version
		from hmac import new

		if not nonce:
			from time import time
			nonce = int(time())

		return {
			'X-Authentication-Key': self.api_key,
			'X-Authentication-Nonce': str(nonce),
			'X-Authentication-Signature': b64encode(new(self.api_secret,
								msg=str(nonce),
								digestmod=sha256).digest()),
			'User-Agent': "PythonClient/{0} ({1}; Python {2})".format(__version__, 
										 platform(True), 
										 python_version())
		}

	def request(self, method, path, data = {}, headers = {}):
		from requests import request

		url = self.api_uri + path
		params = {}
		headers = dict(self.set_headers().items() + headers.items())

		if method == "GET":
			params.update(data)
			return request(method, url, headers=headers, params=params)
		else:
			return request(method, url, headers=headers, params=params, data=json.dumps(data))

	def post(self, path, data = {}):
		return Response(self.request("POST", path, data, {'Content-Type': 'application/json'}))

	def get(self, path, data = {}):
		return Response(self.request("GET", path, data))

	def put(self, path, data = {}):
		return Response(self.request("PUT", path, data, {'Content-Type': 'application/json'}))

	def delete(self, path, data = {}):
		return Response(self.request("DELETE", path, data))

class Response(object):
	def __init__(self, response):
		self.response = response

		try:
			self.content = self.response.json()
		except ValueError:
			self.content = self.response.text

	def ok(self):
		import requests
		return self.response.status_code == requests.codes.ok

	def errors(self):
		if self.ok():
			return {}

		errors = self.content

		if(not isinstance(errors, dict)):
			errors = {"error": errors} # convert to dict for consistency
		elif('errors' in errors):
			errors = errors['errors']

		return errors

	def __getitem__(self, key):
		return self.content[key]
