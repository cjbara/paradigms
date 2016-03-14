import cherrypy
import re, json

class MoviesController(object):
	def __init__(self, db):
		self.db = db

	def GET_ALL_MOVIES(self):
		output = {'result': 'success'}
		output['entries'] = []
		for key in self.db.get_movies():
			output['entries'].append(GET_MOVIE_BY_ID(key))
		return json.dumps(output, encoding='latin-1')

	def GET_MOVIE_BY_ID(self, movie_id):
		output = {}
		value = self.db.get_movie(movie_id)
                if value = None:
		    output['result'] = 'error'
		    output['message'] = 'movie not found'
		    return json.dumps(output, encoding='latin-1')
                else:
                    output = value
		    output['result'] = 'success'
                    output['id'] = movie_id
	            return json.dumps(output, encoding='latin-1')

	def DELETE_ALL_MOVIES(self):
		output = {'result': 'success'}
		data = cherrypy.request.body.fp.read()
                if 'apikey' not in data:
                    return 
                print data
		self.db.delete_all_movies()
		return json.dumps(output, encoding='latin-1')

	def DELETE_MOVIE_BY_ID(self, movie_id):
		output = {'result': 'success'}
		self.db.delete_movie(movie_id)
		return json.dumps(output, encoding='latin-1')
		
	def POST_NEW_MOVIE(self):
		output = {'result': 'success'}
		
		data = cherrypy.request.body.read()
		processed_data = json.loads(data)
		try:
                        new_id = max(self.db.get_movies()) + 1
                        attributes = []
                        attributes.append(processed_data['title'])
                        attributes.append(processed_data['genre'])
                        attributes.append(processed_data['apikey'])
                            
                        self.db.set_movie(new_id, attributes)
                        output['id'] = new_id
                        
		except Exception as ex:
			output['result'] = 'bad parameters, must include genre, title, and apikey'

		return json.dumps(output, encoding='latin-1')
		
	def PUT_NEW_MOVIE(self, key):
		output = {'result': 'success'}
		
		data = cherrypy.request.body.read()
		processed_data = json.loads(data)
		try:
			self.myd[key] = processed_data['value']
		except Exception as ex:
			output['result'] = 'bad parameters to put request'

		return json.dumps(output, encoding='latin-1')
