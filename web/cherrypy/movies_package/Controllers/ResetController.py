# Name: Cory Jbara

import cherrypy
import re, json

class ResetController(object):
	def __init__(self, db):
		self.db = db

	def RESET_ALL_MOVIES(self):
		output = {'result': 'success', 'message': 'reset movies database'}
		data = cherrypy.request.body.read()
		data = json.loads(data)
		if 'apikey' not in data:
			output = {'result': 'error', 'message': 'apikey not supplied'}
			return json.dumps(output, encoding='latin-1')
		self.db.reset_movies()
		print 'Movie 95: ',self.db.get_movie(95)
		return json.dumps(output, encoding='latin-1')

	def RESET_MOVIE_BY_ID(self, movie_id):
		output = {'result': 'success', 'message': 'reset movie with id'+movie_id}
		movie_id = int(movie_id)
		data = cherrypy.request.body.read()
		data = json.loads(data)
		if 'apikey' not in data:
			output = {'result': 'error', 'message': 'apikey not supplied'}
			return json.dumps(output, encoding='latin-1')
		self.db.reset_movie(movie_id)
		return json.dumps(output, encoding='latin-1')
