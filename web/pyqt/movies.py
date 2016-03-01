import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
sys.path.append('/afs/nd.edu/user37/cmc/Public/paradigms/python/local/lib/python2.6/site-packages/requests-2.0.0-py2.6.egg')
import json
import requests

class MoviesQT(QMainWindow):
	"""Encapsulates a small PyQt application"""

	def __init__(self):
		super(MoviesQT, self).__init__()
		self.setWindowTitle("Movie Recommender")
		self.uid = 1

		self.central = MoviesCentral(self.uid, self)
		self.setCentralWidget(self.central)

		self.mainMenu = self.menuBar()
		self.fileMenu = self.mainMenu.addMenu('File')
		self.userMenu = self.mainMenu.addMenu('User')

		self.fileMenu.addAction('Exit', self.exitAction)
		self.userMenu.addAction('View Profile', self.viewProfile)
		self.userMenu.addAction('Set User', self.setUser)

	def setUID(self, uid):
		self.uid = uid
		print "New uid =",self.uid

	def exitAction(self):
		sys.exit()

	def viewProfile(self):
		self.profile = UserProfile(self.uid)
		self.profile.show()
		print "View Profile"

	def setUser(self):
		self.newUser = NewUser(self)
		self.newUser.show()
		print "Set User"

class UserProfile(QWidget):
	"""Class that displays the user information in a widget"""
	def __init__(self, uid):
		super(UserProfile, self).__init__()
		self.uid = uid
		self.setWindowTitle("User Profile: " + str(self.uid))

		self.getInfo()
	
		self.idLabel = QLabel("ID: " + str(self.uid))
		self.genderLabel = QLabel("Gender: " + self.gender)
		self.zipLabel = QLabel("Zipcode: " + str(self.zipcode))
		self.ageLabel = QLabel("Age: " + str(self.age))

		self.layout = QVBoxLayout()
		self.layout.addWidget(self.idLabel)
		self.layout.addWidget(self.genderLabel)
		self.layout.addWidget(self.zipLabel)
		self.layout.addWidget(self.ageLabel)
		
		self.setLayout(self.layout)

	def getInfo(self):
		SITE_URL = 'http://student02.cse.nd.edu:40001'
		USER_URL = '/users/'
		r = requests.get(SITE_URL + USER_URL + str(self.uid))
		resp = json.loads(r.content)
		self.age = resp['age']
		self.gender = resp['gender']
		self.zipcode = resp['zipcode']

class NewUser(QWidget):
	"""Class that allows you to set the user in a new widget"""
	def __init__(self, parent = None):
		super(NewUser, self).__init__()
		self.parent = parent
		self.setWindowTitle("Get User Profile")

		self.idLabel = QLabel("User ID:")
		self.newID = QLineEdit()
		self.submit = QPushButton("Submit")
		self.submit.clicked.connect(self.submitAction)
		self.cancel = QPushButton("Cancel")
		self.cancel.clicked.connect(self.cancelAction)

		self.layout = QVBoxLayout()
		self.layout2 = QHBoxLayout()
		self.layout.addWidget(self.idLabel)
		self.layout.addWidget(self.newID)
		
		self.layout2.addWidget(self.submit)
		self.layout2.addWidget(self.cancel)
		
		self.layout.addLayout(self.layout2)
		self.setLayout(self.layout)

	def submitAction(self):
		if str(self.newID.text()).isdigit():
			if isinstance( int(self.newID.text()), int ):
				SITE_URL = 'http://student02.cse.nd.edu:40001'
				USER_URL = '/users/'
				r = requests.get(SITE_URL + USER_URL + str(int(self.newID.text())))
				resp = json.loads(r.content)
				if resp['result'] == 'success':	
					self.parent.setUID(int(self.newID.text()))
					self.newID.setText("")
					self.hide()
				else:
					self.idLabel.setText("User ID: Not a Valid User ID")
			else: 
				self.idLabel.setText("User ID: Must be an Integer")
		else: 
			self.idLabel.setText("User ID: Must be an Integer")
			
	
	def cancelAction(self):
		self.idLabel.setText("User ID:")
		self.hide()
		print "Cancel"

class MoviesCentral(QWidget):
	def __init__(self, uid, parent = None):
		super(MoviesCentral, self).__init__(parent)
		self.apiKey = 'OSXCiF2wcf'
		self.uid = uid
		self.count = 0
		self.imagesDirectory = "/afs/nd.edu/user37/cmc/Public/cse332_sp16/cherrypy/data/images/"
		self.SITE_URL = 'http://student02.cse.nd.edu:40001'
		self.REC_URL = '/recommendations/'
		self.MOVIE_URL = '/movies/'
		self.RATING_URL = '/ratings/'

		self.getMovie()
		self.count += 1
		
	def setUID(self, uid):
		self.uid = uid

	def getMovie(self):
		r = requests.get(self.SITE_URL + self.REC_URL + str(self.uid))
		resp = json.loads(r.content)
		self.mid = resp['movie_id']

		r = requests.get(self.SITE_URL + self.MOVIE_URL + str(self.mid))
		resp = json.loads(r.content)
		self.title = resp['title']
		self.genre = resp['genres']
		self.image = resp['img']

		r = requests.get(self.SITE_URL + self.RATING_URL + str(self.mid))
		resp = json.loads(r.content)
		self.rating = resp['rating']
		self.updateDisplay()

	def updateDisplay(self):
		if self.count == 0:
			self.layout = QHBoxLayout()
			self.upbutton = QPushButton("Up")
			self.upbutton.clicked.connect(self.upVote)
			self.downbutton = QPushButton("Down")
			self.downbutton.clicked.connect(self.downVote)

			self.posterLayout = QVBoxLayout()
			self.titleLabel = QLabel(self.title)
			self.poster = QLabel()
			self.pixmap = QPixmap(self.imagesDirectory + self.image)
			self.poster.setPixmap(self.pixmap)
			self.genreLabel = QLabel(self.genre)
			self.ratingLabel = QLabel(str(self.rating))
			self.ratingLabel.setText("%.3f" % (self.rating))

			self.posterLayout.addWidget(self.titleLabel)
			self.posterLayout.addWidget(self.poster)
			self.posterLayout.addWidget(self.genreLabel)
			self.posterLayout.addWidget(self.ratingLabel)

			self.layout.addWidget(self.upbutton)
			self.layout.addLayout(self.posterLayout)
			self.layout.addWidget(self.downbutton)

			self.setLayout(self.layout)
		else:
			self.titleLabel.setText(self.title)
			self.genreLabel.setText(self.genre)
			self.ratingLabel.setText("%.3f" % (self.rating))
			self.pixmap = QPixmap(self.imagesDirectory + self.image)
			self.poster.setPixmap(self.pixmap)

	def upVote(self):
		rec = {}
		rec['movie_id'] = self.mid
		rec['rating'] = 5
		rec['apikey'] = self.apiKey
		r = requests.put(self.SITE_URL + self.REC_URL + str(self.uid), data = json.dumps(rec))
		print "Upvote"
		self.getMovie()

	def downVote(self):
		rec = {}
		rec['movie_id'] = self.mid
		rec['rating'] = 1
		rec['apikey'] = self.apiKey
		r = requests.put(self.SITE_URL + self.REC_URL + str(self.uid), data = json.dumps(rec))
		print "Down Vote"
		self.getMovie()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	gui = MoviesQT()
	gui.show()
	sys.exit(app.exec_())
