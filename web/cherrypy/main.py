import cherrypy
from movies_package import *

def start_service():
	moviesController = MoviesController()

	#Create the routes
	dispatcher = cherrypy.dispatch.RoutesDispatcher()
	
#===================== MOVIES ROUTES ===========================
    #================= ALL MOVIES ==============================
	#GET all movies
	dispatcher.connect('get_all_movies','/movies/', controller = moviesController, action = 'GET_ALL_MOVIES', conditions = dict(method = ['GET']))

	#POST new movie
	dispatcher.connect('post_new_movie','/movies/', controller = moviesController, action = 'POST_NEW_MOVIE', conditions = dict(method = ['POST']))

	#DELETE all movies
	dispatcher.connect('delete_all_movies','/movies/', controller = moviesController, action = 'DELETE_ALL_MOVIES', conditions = dict(method = ['DELETE']))

    #================= SINGLE MOVIES ===========================
        #GET movie by Id
	dispatcher.connect('get_movie_by_id','/movies/:movie_id', controller = moviesController, action = 'GET_MOVIE_BY_ID', conditions = dict(method = ['GET']))

        #PUT new movie
	dispatcher.connect('put_new_movie','/movies/:movie_id', controller = moviesController, action = 'PUT_NEW_MOVIE', conditions = dict(method = ['PUT']))

        #DELETE movie by Id
	dispatcher.connect('delete_movie_by_id','/movies/:movie_id', controller = moviesController, action = 'DELETE_MOVIE_BY_ID', conditions = dict(method = ['DELETE']))

#===================== USERS ROUTES ===========================
#===================== RECOMMENDATIONS ROUTES ===========================
#===================== RATINGS ROUTES ===========================
#===================== RESET ROUTES ===========================

	#Do the configuration for the server
	conf = { 'global': {'server.socket_host': 'student00.cse.nd.edu', 'server.socket_port': 40062}, '/': {'request.dispatch': dispatcher } }
	cherrypy.config.update(conf)
	app = cherrypy.tree.mount(None, config = conf)
	cherrypy.quickstart(app)

if __name__ == '__main__':
	start_service()
