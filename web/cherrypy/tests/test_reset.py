import unittest
import requests
import json

class TestReset(unittest.TestCase):

	SITE_URL = 'http://student00.cse.nd.edu:40062'
	RESET_URL = SITE_URL + '/reset/'

	def test_reset_data(self):
		m = {}
		m['apikey'] = 'AAAAAAAB'
		r = requests.put(self.RESET_URL, data = m)

if __name__ == "__main__":
	unittest.main()

