# Name: Cory Jbara

import cherrypy
import re, json

class RatingsController(object):
	def __init__(self, db):
		self.db = db

	def GET_RATING_BY_ID(self, movie_id):
		output = {}
		movie_id = int(movie_id)
		rating = self.db.get_rating(movie_id)
		if rating == 0:
			output['result'] = 'error'
			output['message'] = 'rating not found'
			return json.dumps(output, encoding='latin-1')
		else:
			output['rating'] = rating
			output['result'] = 'success'
			output['movie_id'] = movie_id
			return json.dumps(output, encoding='latin-1')
