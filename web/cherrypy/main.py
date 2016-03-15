# Name: Cory Jbara

import cherrypy
from movies_package import *

def start_service():
	movies_db = MovieDatabase()
	moviesController = MoviesController(movies_db)
	usersController = UsersController(movies_db)
	recommendationsController = RecommendationsController(movies_db)
	ratingsController = RatingsController(movies_db)
	resetController = ResetController(movies_db)

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
	#================= ALL USERS ==============================
	#GET all users
	dispatcher.connect('get_all_users','/users/', controller = usersController, action = 'GET_ALL_USERS', conditions = dict(method = ['GET']))

	#POST new user
	dispatcher.connect('post_new_user','/users/', controller = usersController, action = 'POST_NEW_USER', conditions = dict(method = ['POST']))

	#DELETE all users
	dispatcher.connect('delete_all_users','/users/', controller = usersController, action = 'DELETE_ALL_USERS', conditions = dict(method = ['DELETE']))

	#================= SINGLE USERS ===========================
	#GET user by Id
	dispatcher.connect('get_user_by_id','/users/:user_id', controller = usersController, action = 'GET_USER_BY_ID', conditions = dict(method = ['GET']))

	#PUT new user
	dispatcher.connect('put_new_user','/users/:user_id', controller = usersController, action = 'PUT_NEW_USER', conditions = dict(method = ['PUT']))

	#DELETE user by Id
	dispatcher.connect('delete_user_by_id','/users/:user_id', controller = usersController, action = 'DELETE_USER_BY_ID', conditions = dict(method = ['DELETE']))

#===================== RECOMMENDATIONS ROUTES ===========================
	#GET recommendation by Id
	dispatcher.connect('get_rec_by_id','/recommendations/:user_id', controller = recommendationsController, action = 'GET_REC_BY_ID', conditions = dict(method = ['GET']))

	#PUT new recommendation
	dispatcher.connect('put_new_rec','/recommendations/:user_id', controller = recommendationsController, action = 'PUT_NEW_REC', conditions = dict(method = ['PUT']))

	#DELETE all recommendations
	dispatcher.connect('delete_all_recs','/recommendations/', controller = recommendationsController, action = 'DELETE_ALL_RECS', conditions = dict(method = ['DELETE']))

#===================== RATINGS ROUTES ===========================
	#GET rating by Id
	dispatcher.connect('get_rating_by_id','/ratings/:movie_id', controller = ratingsController, action = 'GET_RATING_BY_ID', conditions = dict(method = ['GET']))

#===================== RESET ROUTES ===========================
	#PUT reset All
	dispatcher.connect('reset_all','/reset/', controller = resetController, action = 'RESET_ALL_MOVIES', conditions = dict(method = ['PUT']))
	#PUT reset
	dispatcher.connect('reset_id','/reset/:movie_id', controller = resetController, action = 'RESET_MOVIE_BY_ID', conditions = dict(method = ['PUT']))

#===================== SERVER CONFIGURATION ==================
	#Do the configuration for the server
	conf = { 'global': {'server.socket_host': 'student00.cse.nd.edu', 'server.socket_port': 40062}, '/': {'request.dispatch': dispatcher } }
	cherrypy.config.update(conf)
	app = cherrypy.tree.mount(None, config = conf)
	cherrypy.quickstart(app)

if __name__ == '__main__':
	start_service()
