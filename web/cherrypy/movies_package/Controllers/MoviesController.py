# Name: Cory Jbara

import cherrypy
import re, json

class MoviesController(object):
	def __init__(self, db):
		self.db = db

	def GET_ALL_MOVIES(self):
		output = {'result': 'success'}
		output['movies'] = []
		for movie_id in self.db.get_movies():
			value = self.db.get_movie(movie_id)
			if value == None:
				value = {}
				value['result'] = 'error'
				value['message'] = 'movie not found'
			else:
				value['result'] = 'success'
				value['id'] = movie_id
			output['movies'].append(value)
		return json.dumps(output, encoding='latin-1')

	def GET_MOVIE_BY_ID(self, movie_id):
		output = {}
		movie_id = int(movie_id)
		value = self.db.get_movie(movie_id)
		if value == None:
			output['result'] = 'error'
			output['message'] = 'movie not found'
			return json.dumps(output, encoding='latin-1')
		else:
			output = value
			output['result'] = 'success'
			output['id'] = movie_id
			return json.dumps(output, encoding='latin-1')

	def DELETE_ALL_MOVIES(self):
		output = {'result': 'success', 'message': 'deleted all movies in database'}
		data = cherrypy.request.body.fp.read()
		data = json.loads(data)
		if 'apikey' not in data:
			output = {'result': 'error', 'message': 'apikey not supplied'}
			return json.dumps(output, encoding='latin-1')
		self.db.delete_all_movies()
		return json.dumps(output, encoding='latin-1')

	def DELETE_MOVIE_BY_ID(self, movie_id):
		output = {'result': 'success', 'message': 'deleted movie with id: '+movie_id}
		movie_id = int(movie_id)
		data = cherrypy.request.body.fp.read()
		data = json.loads(data)
		if 'apikey' not in data:
			output = {'result': 'error', 'message': 'apikey not supplied'}
			return json.dumps(output, encoding='latin-1')
		self.db.delete_movie(movie_id)
		return json.dumps(output, encoding='latin-1')
		
	def POST_NEW_MOVIE(self):
		output = {'result': 'success'}
		
		data = cherrypy.request.body.read()
		processed_data = json.loads(data)
		try:
			if len(self.db.get_movies()) == 0:
				new_id = 1
			else:
				new_id = max(self.db.get_movies()) + 1
			attributes = []
			attributes.append(processed_data['title'])
			attributes.append(processed_data['genres'])
			attributes.append(processed_data['apikey'])
				
			self.db.set_movie(new_id, attributes)
			output['id'] = new_id
						
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = 'bad parameters, must include genres, title, and apikey'
		return json.dumps(output, encoding='latin-1')
		
	def PUT_NEW_MOVIE(self, movie_id):
		output = {'result': 'success'}
		
		movie_id = int(movie_id)
		data = cherrypy.request.body.read()
		processed_data = json.loads(data)
		try:
			attributes = []
			attributes.append(processed_data['title'])
			attributes.append(processed_data['genres'])
			attributes.append(processed_data['apikey'])
				
			self.db.set_movie(movie_id, attributes)
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = 'bad parameters, must include genres, title, and apikey'
		return json.dumps(output, encoding='latin-1')
