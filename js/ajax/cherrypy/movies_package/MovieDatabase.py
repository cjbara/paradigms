#Name: Cory Jbara
#Python Movie Database

class MovieDatabase(object):
	"""Class that will store information about movies"""
	
	def __init__(self):
		"""Initializes dictionaries for users, movies, and ratings"""
		self.reset_movies()

#================ Reset Methods ====================
	def reset_movies(self):
		"""Resets entire database"""
		self.movies = {}
		self.users = {}
		self.ratings = {}
		self.load_movies()
		self.load_movie_images()
		self.load_users()
		self.load_ratings()

	def reset_movie(self, movie_id):
		"""Resets one movie from dat file"""
		movie_id = int(movie_id)
		movie_file = 'data/movies.dat'
		f = open(movie_file, 'r')
		for line in f:
			line = line.strip()
			line = line.split('::')
			mid = int(line[0])
			if mid == movie_id:
				title = line[1]
				genres = line[2]
				self.movies[mid] = { 'title': title, 'genres': genres }
		f.close()

		image_file = 'data/images.dat'
		f = open(image_file, 'r')
		for line in f:
			line = line.strip()
			line = line.split('::')
			mid = int(line[0])
			if mid == movie_id:
				image = line[2]
				if image == '':
					image = 'default.jpg'
				self.movies[mid]['img'] = image

#================ Movies Methods ====================
	def load_movies(self):
		"""Loads movies from file movie_file into database"""
		movie_file = 'data/movies.dat'
		f = open(movie_file, 'r')
		for line in f:
			line = line.strip()
			line = line.split('::')
			mid = int(line[0])
			title = line[1]
			genres = line[2]
			self.movies[mid] = { 'title': title, 'genres': genres }
		f.close()

	def load_movie_images(self):
		"""Loads the images into the movie database"""
		image_file = 'data/images.dat'
		f = open(image_file, 'r')
		for line in f:
			line = line.strip()
			line = line.split('::')
			mid = int(line[0])
			image = line[2]
			if image == '':
				image = 'default.jpg'
			self.movies[mid]['img'] = image
			
	def get_movie(self, mid):
		"""Returns the movie with key mid"""
		if mid in self.movies: 
			return self.movies[mid]
		else:
			return None

	def get_movies(self):
		"""Returns a list of all movies IDs"""
		return self.movies.keys()

	def set_movie(self, mid, tg): #, [title, genres]):
		"""Updates or creates new movie with attributes"""
		self.movies[mid] = { 'title': tg[0], 'genres': tg[1] }

	def delete_movie(self, mid):
		"""Deletes movie from db with ID = mid"""
		if mid in self.movies: del self.movies[mid]

	def delete_all_movies(self):
		"""Deletes all movies from db"""
		self.movies = {}

#================ Users Methods ====================
	def load_users(self):
		"""Loads users from file into database"""
		users_file = 'data/users.dat'
		f = open(users_file, 'r')
		for line in f:
			line = line.strip()
			line = line.split('::')
			uid = int(line[0])
			gender = line[1]
			age = int(line[2])
			occupation = int(line[3])
			zipcode = line[4]
			self.users[uid] = { 'gender': gender, 'age': age, 'occupation': occupation, 'zipcode': zipcode }
		f.close()

	def get_user(self, uid):
		"""Returns the user with key uid"""
		if uid in self.users: 
			return self.users[uid]
		else:
			return None

	def get_users(self):
		"""Returns a list of all users IDs"""
		return self.users.keys()

	def set_user(self, uid, params): #, [gender, age, occupationcode, zipcode]):
		"""Updates or creates new user with attributes"""
		gender = params[0]
		age = params[1]
		occupation = params[2]
		zipcode = params[3]
		self.users[uid] = {'gender': gender, 'age': age, 'occupation': occupation, 'zipcode': zipcode }

	def delete_all_users(self):
		"""Deletes all users from db"""
		self.users = {}

	def delete_user(self, uid):
		"""Deletes user from db with ID = uid"""
		if uid in self.users: del self.users[uid]

#================ Ratings Methods ====================
	def load_ratings(self):
		"""Loads ratings from file into database"""
		ratings_file = 'data/ratings.dat'
		f = open(ratings_file, 'r')
		for line in f:
			line = line.split('::')
			mid = int(line[1])
			uid = int(line[0])
			rating = int(line[2])
			if mid in self.ratings:
				self.ratings[mid][uid] = rating
			else:
				self.ratings[mid] = { uid: rating }
		f.close()

	def get_rating(self, mid):
		"""Returns the rating with key mid"""
		if mid in self.ratings:
			avg = 0.0
			count = 0
			for r in self.ratings[mid]:
				count += 1
				avg += self.ratings[mid][r]
			avg = avg / count
			return avg
		else:
			return 0

#================ Recommendations Methods ====================
	def get_recommendation(self, user_id):
		"""Gets a recommendation for a particular user"""
		if self.get_user(user_id) == None:
			return None

		movies = self.ratings
		for movie_id in movies.keys():
			if user_id in self.ratings[movie_id].keys():
				del movies[movie_id]

		if len(movies.keys()) > 0:
			best_movie = self.get_highest_rated_movie(movies.keys())
			return best_movie
		return 0

	def get_highest_rated_movie(self, remaining_movies):
		"""Returns ID of the movie with the highest rating"""
		movies = {}
		m = 0
		for mid in remaining_movies:
			movies[mid] = self.get_rating(mid)
		m = max(movies.values())
		for mid in movies.keys():
			if movies[mid] == m:
				return mid

	def delete_all_recommendations(self):
		"""Deletes the ratings dictionary"""
		self.ratings = {}

	def set_recommendation(self, user_id, attributes): #[movie_id, rating]
		"""Sets a rating"""
		movie_id = attributes[0]
		rating = attributes[1]
		self.set_user_movie_rating(user_id, movie_id, rating)

	def set_user_movie_rating(self, uid, mid, rating):
		"""Updates or creates new rating for mid by uid"""
		if mid in self.movies:
			self.ratings[mid][uid] = rating
		else:
			self.ratings[mid] = { uid: rating }

	def get_user_movie_rating(self, uid, mid):
		"""Returns the rating of a movie by a user"""
		return self.ratings[mid][uid]

	def delete_all_ratings(self):
		"""Deletes all ratings from database"""
		self.ratings = {}

	
