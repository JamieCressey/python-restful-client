import sys
if sys.version_info < (2, 7):
	import unittest2 as unittest
else:
	import unittest

from RestfulClient.api import ApiClient

class ApiClientTest(unittest.TestCase):
	def setUp(self):
		self.api = ApiClient('#key', '#secret', 'http://localhost:5000')

	def test_version(self):
		self.assertRegexpMatches(self.api.version(), '\d.\d*')
