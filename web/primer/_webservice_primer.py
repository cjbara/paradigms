import sys
sys.path.append('/afs/nd.edu/user37/cmc/Public/paradigms/python/local/lib/python2.6/site-packages/requests-2.0.0-py2.6.egg')
import requests
import json

class _webservice_primer(object):
	"""Class for the movie web service"""

	def __init__(self, apikey):
		self.API_KEY = apikey
		self.SITE_URL = 'http://student02.cse.nd.edu:40001'
		self.MOVIES_URL = self.SITE_URL + '/movies/'
		self.RESET_URL = self.SITE_URL + '/reset/'
	
	def get_movie(self, mid):
		mid = str(mid)
		r = requests.get(self.MOVIES_URL + mid)
		resp = json.loads(r.content)
		return resp

	def set_movie_title(self, mid, title):
		movie = self.get_movie(mid)
		movie['title'] = title
		movie['apikey'] = self.API_KEY
		r = requests.put(self.MOVIES_URL + str(mid), data = json.dumps(movie))
		resp = json.loads(r.content)
		return resp

	def delete_movie(self, mid):
		data = {}
		data['apikey'] = self.API_KEY
		r = requests.delete(self.MOVIES_URL + str(mid), data = json.dumps(data))
		resp = json.loads(r.content)
		return resp

	def reset_movie(self, mid):
		mydata = {}
		mydata['apikey'] = self.API_KEY
		r = requests.put(self.RESET_URL + str(mid), data = json.dumps(mydata))
		resp = json.loads(r.content)
		return resp

if __name__ == "__main__":
	MID = 32
	API_KEY = 'OSXCiF2wcf'
	ws = _webservice_primer(API_KEY)
	print ws.get_movie(MID)
	print ws.set_movie_title(MID, "Stuff")
	print ws.get_movie(MID)
	print ws.delete_movie(MID)
	print ws.get_movie(MID)
	print ws.reset_movie(MID)
	print ws.get_movie(MID)
	
