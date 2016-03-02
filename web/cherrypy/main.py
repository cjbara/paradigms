import cherrypy
from dcontlib import DictionaryController

def start_service():
	dictionaryController = DictionaryController()

	#Cretae the routes
	dispatcher = cherrypy.dispatch.RoutesDispatcher()
	
	#GET Methods
	dispatcher.connect('dict_get','/dictionary/', controller = dictionaryController, action = 'GET_DICT', conditions = dict(method = ['GET']))
	dispatcher.connect('dict_get_key','/dictionary/:key', controller = dictionaryController, action = 'GET_KEY', conditions = dict(method = ['GET']))

	#DELETE Methods
	dispatcher.connect('dict_delete','/dictionary/', controller = dictionaryController, action = 'DELETE_DICT', conditions = dict(method = ['DELETE']))
	dispatcher.connect('dict_delete_key','/dictionary/:key', controller = dictionaryController, action = 'DELETE_KEY', conditions = dict(method = ['DELETE']))

	#POST/PUT Methods
	dispatcher.connect('dict_post','/dictionary/', controller = dictionaryController, action = 'POST_DICT', conditions = dict(method = ['POST']))
	dispatcher.connect('dict_put_key','/dictionary/:key', controller = dictionaryController, action = 'PUT_KEY', conditions = dict(method = ['PUT']))

	#Do the configuration for the server
	conf = { 'global': {'server.socket_host': 'student00.cse.nd.edu', 'server.socket_port': 40062}, '/': {'request.dispatch': dispatcher } }
	cherrypy.config.update(conf)
	app = cherrypy.tree.mount(None, config = conf)
	cherrypy.quickstart(app)

if __name__ == '__main__':
	start_service()
