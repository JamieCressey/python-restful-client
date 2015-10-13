import sys
if sys.version_info < (2, 7):
	import unittest2 as unittest
else:
	import unittest

from RestfulClient.api import ApiClient
from time import time

class CreateBookTest(unittest.TestCase):
	def setUp(self):
		self.api = ApiClient('#your_api_key', '#your_api_secret', 'http://restful.jamiecressey.com:5000')
		self.title = str(int(time()))

	def test_createBook(self):
		_resp = self.api.post('/books/', {
			'title': self.title
		})
		self.assertEqual(_resp.ok(), True)
		self.assertDictContainsSubset({'title': self.title}, _resp.content)

		_resp = self.api.get('/book/{}/'.format(self.title))	
		self.assertEqual(_resp.ok(), True)
		self.assertDictContainsSubset({'title': self.title}, _resp.content)

		_resp = self.api.put('/book/{}/'.format(self.title), {
			'author': 'Jamie Cressey'
		})
		self.assertEqual(_resp.ok(), True)
		self.assertDictContainsSubset({'author': 'Jamie Cressey'}, _resp.content)

		_resp = self.api.put('/book/{}/'.format(self.title), {
			'release_date': '01/01/2001'
		})
		self.assertEqual(_resp.ok(), True)
		self.assertDictContainsSubset({'release_date': '01/01/2001'}, _resp.content)

		_resp = self.api.get('/book/{}/'.format(self.title))	
		self.assertEqual(_resp.ok(), True)
		self.assertDictContainsSubset({'title': self.title, 'author': 'Jamie Cressey', 'release_date': '01/01/2001'}, _resp.content)

		_resp = self.api.delete('/book/{}/'.format(self.title))	
		self.assertEqual(_resp.ok(), True)
		self.assertDictContainsSubset({'message': 'Book deleted'}, _resp.content)
