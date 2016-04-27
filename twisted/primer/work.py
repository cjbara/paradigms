# Paradigms Twisted Primer
# Cory Jbara

from twisted.internet.protocol import Factory
from twisted.internet.protocol import ClientFactory
from twisted.internet.protocol import Protocol
from twisted.protocols.basic import LineReceiver
from twisted.internet.tcp import Port
from twisted.internet import reactor
from twisted.internet.defer import DeferredQueue

#======================================================================
class Work(object):
	def __init__(self):
		self.home_server = 'student00.cse.nd.edu'
		self.home_port_1 = 40062
		self.home_port_2 = 41062
		self.student_server = 'student00.cse.nd.edu'
		self.student_port = 22
		self.home_queue = DeferredQueue()
		self.student_queue = DeferredQueue()

	def connect(self):
		reactor.connectTCP(self.home_server, self.home_port_1, CommandConnToHomeFactory(self))
		reactor.run()

#======================================================================
class CommandConnToHome(LineReceiver):
	def __init__(self, addr, work):
		self.addr = addr
		self.work = work

	def connectionMade(self):
		print 'Command connection made to HOME'

	def connectionLost(self, reason):
		print 'Command connection lost to HOME'

	def dataReceived(self, data):
		"""Data received from home connection, this means client has connected to home, so create a new DataConnToHome"""
		reactor.connectTCP(self.work.home_server, self.work.home_port_2, DataConnToHomeFactory(self.work))

#======================================================================
class CommandConnToHomeFactory(ClientFactory):
	def __init__(self, work):
		self.work = work

	def buildProtocol(self, addr):
		return CommandConnToHome(addr, self.work)

#======================================================================
class DataConnToHome(LineReceiver):
	def __init__(self, addr, work):
		self.addr = addr
		self.work = work

	def connectionMade(self):
		print 'Data connection made to HOME'
		# Add callback then connect to the student server
		self.work.home_queue.get().addCallback(self.sendToHome)
		reactor.connectTCP(self.work.student_server, self.work.student_port, ConnToStudentFactory(self.work))

	def connectionLost(self, reason):
		print 'Data connection lost to HOME'

	def dataReceived(self, data):
		"""Data received from home connection, forward to student"""
		self.work.student_queue.put(data)

	def sendToHome(self, data):
		print 'Sending data to HOME'
		self.sendLine(data)
		self.work.home_queue.get().addCallback(self.sendToHome)

#======================================================================
class DataConnToHomeFactory(ClientFactory):
	def __init__(self, work):
		self.work = work

	def buildProtocol(self, addr):
		return DataConnToHome(addr, self.work)

#======================================================================
class ConnToStudent(Protocol):
	def __init__(self, addr, work):
		self.addr = addr
		self.work = work

	def connectionMade(self):
		print 'Connection made to STUDENT'
		# Add callback
		self.work.student_queue.get().addCallback(self.sendToStudent)

	def connectionLost(self, reason):
		print 'Connection lost to STUDENT'

	def dataReceived(self, data):
		"""Data received back from the student machine, forward to home"""
		print 'Received data from STUDENT'
		self.work.home_queue.put(data)

	def sendToStudent(self, data):
		self.transport.write(data)
		self.work.student_queue.get().addCallback(self.sendToStudent)

#======================================================================
class ConnToStudentFactory(ClientFactory):
	def __init__(self, work):
		self.work = work

	def buildProtocol(self, addr):
		return ConnToStudent(addr, self.work)

if __name__ == '__main__':
	work = Work()
	work.connect()
