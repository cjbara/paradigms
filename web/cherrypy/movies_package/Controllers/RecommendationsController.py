# Name: Cory Jbara

import cherrypy
import re, json

class RecommendationsController(object):
	def __init__(self, db):
		self.db = db

	def GET_REC_BY_ID(self, user_id):
		output = {}
		user_id = int(user_id)
		movie_id = self.db.get_recommendation(user_id)
		if movie_id == None:
			output['result'] = 'error'
			output['message'] = 'user not found'
			return json.dumps(output, encoding='latin-1')
		elif movie_id == 0:
			output['result'] = 'success'
			output['message'] = 'No more movies to recommend'
			return json.dumps(output, encoding='latin-1')
		else:
			output['result'] = 'success'
			output['movie_id'] = movie_id
			return json.dumps(output, encoding='latin-1')

	def PUT_NEW_REC(self, user_id):
		output = {'result': 'success'}
		
		user_id = int(user_id)
		data = cherrypy.request.body.read()
		processed_data = json.loads(data)
		print processed_data
		try:
			attributes = []
			attributes.append(processed_data['movie_id'])
			attributes.append(processed_data['rating'])
			attributes.append(processed_data['apikey'])
				
			self.db.set_recommendation(user_id, attributes)
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = 'bad parameters, must include movie_id, rating, and apikey'
		return json.dumps(output, encoding='latin-1')

	def DELETE_ALL_RECS(self):
		output = {'result': 'success', 'message': 'deleted all recommendations in database'}
		data = cherrypy.request.body.fp.read()
		data = json.loads(data)
		if 'apikey' not in data:
			output = {'result': 'error', 'message': 'apikey not supplied'}
			return json.dumps(output, encoding='latin-1')
		self.db.delete_all_recommendations()
		return json.dumps(output, encoding='latin-1')
