import cherrypy
import re, json

class DictionaryController(object):
	def __init__(self):
		self.myd = dict()

	def GET_DICT(self):
		output = {'result': 'success'}
		output['entries'] = []
		for key in self.myd:
			output['entries'].append({'key': key, 'value': self.myd[key]})
		return json.dumps(output, encoding='latin-1')

	def GET_KEY(self, key):
		output = {'result': 'success'}
		try:
			value = self.myd[key]
			output['key'] = key
			output['value'] = value
		except KeyError as ex:
			output['result'] = 'error'
			output['message'] = 'key not found'
		return json.dumps(output, encoding='latin-1')

	def DELETE_DICT(self):
		output = {'result': 'success'}
		self.myd = {}
		return json.dumps(output, encoding='latin-1')

	def DELETE_KEY(self, key):
		output = {'result': 'success'}
		self.myd.pop(key)
		return json.dumps(output, encoding='latin-1')
		
	def POST_DICT(self):
		output = {'result': 'success'}
		
		data = cherrypy.request.body.read()
		processed_data = json.loads(data)
		try:
			self.myd[processed_data['key']] = processed_data['value']
		except Exception as ex:
			output['result'] = 'bad parameters to post request'

		return json.dumps(output, encoding='latin-1')
		
	def PUT_KEY(self, key):
		output = {'result': 'success'}
		
		data = cherrypy.request.body.read()
		processed_data = json.loads(data)
		try:
			self.myd[key] = processed_data['value']
		except Exception as ex:
			output['result'] = 'bad parameters to put request'

		return json.dumps(output, encoding='latin-1')
