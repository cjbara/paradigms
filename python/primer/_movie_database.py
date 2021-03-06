#Name: Cory Jbara
#Python Movie Database

class _movie_database(object):
	"""Class that will store information about movies"""
	
	def __init__(self):
		"""Initializes empty dictionaries for users, movies, and ratings"""
		self.movies = {}
		self.users = {}
		self.ratings = {}

#================ Movies Methods ====================
	def load_movies(self, movie_file):
		"""Loads movies from file movie_file into database"""
		f = open(movie_file, 'r')
		for line in f:
			line = line.strip()
			line = line.split('::')
			mid = int(line[0])
			name = line[1]
			genre = line[2]
			self.movies[mid] = { 'name': name, 'genre': genre }
		f.close()
		
	def get_movie(self, mid):
		"""Returns the movie with key mid"""
		if mid in self.movies: 
			return [self.movies[mid]['name'], self.movies[mid]['genre']]
		else:
			return None

	def get_movies(self):
		"""Returns a list of all movies IDs"""
		return self.movies.keys()

	def set_movie(self, mid, tg): #, [title, genres]):
		"""Updates or creates new movie with attributes"""
		self.movies[mid] = { 'name': tg[0], 'genre': tg[1] }

	def delete_movie(self, mid):
		"""Deletes movie from db with ID = mid"""
		if mid in self.movies: del self.movies[mid]

#================ Users Methods ====================
	def load_users(self, users_file):
		"""Loads users from file into database"""
		f = open(users_file, 'r')
		for line in f:
			line = line.strip()
			line = line.split('::')
			uid = int(line[0])
			gender = line[1]
			age = int(line[2])
			occupation = int(line[3])
			zipcode = line[4]
			self.users[uid] = { 'gender': gender, 'age': age, 'occupation': occupation, 'zip': zipcode }
		f.close()

	def get_user(self, uid):
		"""Returns the user with key uid"""
		if uid in self.users: 
			u = self.users[uid]
			return [u['gender'], u['age'], u['occupation'], u['zip']]
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
		self.users[uid] = {'gender': gender, 'age': age, 'occupation': occupation, 'zip': zipcode }

	def delete_user(self, uid):
		"""Deletes user from db with ID = uid"""
		if uid in self.users: del self.users[uid]

#================ Ratings Methods ====================
	def load_ratings(self, ratings_file):
		"""Loads ratings from file into database"""
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

	def get_highest_rated_movie(self):
		"""Returns ID of the movie with the highest rating"""
		movies = {}
                m = 0
		for mid in self.movies.keys():
			movies[mid] = self.get_rating(mid)
                for rating in movies:
                    if movies[rating] > m:
                        m = rating
		for mid in movies.keys():
			if movies[mid] == m:
				return mid

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

	
