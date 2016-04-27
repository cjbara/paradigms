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
class Home(object):
	def __init__(self):
		self.client_server = 'localhost'
		self.client_port = 9452
		self.work_server = 'student00.cse.nd.edu'
		self.work_port_1 = 40062
		self.work_port_2 = 41062
		self.client_queue = DeferredQueue()
		self.work_queue = DeferredQueue()

	def listen(self):
		reactor.listenTCP(self.client_port, ConnToClientFactory(self))
		reactor.listenTCP(self.work_port_1, CommandConnToWorkFactory(self))
		reactor.run()

#======================================================================
class CommandConnToWork(Protocol):
	def __init__(self, addr, home):
		self.addr = addr
		self.home = home

	def connectionMade(self):
		print 'Command connection received from WORK'
		# Add callback
		self.home.work_queue.get().addCallback(self.makeDataConnectionToWork)
		reactor.listenTCP(self.home.work_port_2, DataConnToWorkFactory(self.home))

	def connectionLost(self, reason):
		print 'Command connection lost from WORK'

	def dataReceived(self, data):
		"""Data received back from the work machine, this shouldn't ever be called"""
		print 'This should not be happening'

	def makeDataConnectionToWork(self, data):
		self.transport.write(data)

#======================================================================
class CommandConnToWorkFactory(Factory):
	def __init__(self, home):
		self.home = home

	def buildProtocol(self, addr):
		return CommandConnToWork(addr, self.home)

#======================================================================
class DataConnToWork(Protocol):
	def __init__(self, addr, home):
		self.addr = addr
		self.home = home

	def connectionMade(self):
		print 'Data connection received from WORK'
		# Add callback
		self.home.work_queue.get().addCallback(self.sendToWork)

	def connectionLost(self, reason):
		print 'Data connection lost from WORK'

	def dataReceived(self, data):
		"""Data received back from the work machine, forward to client"""
		print 'Received data from WORK'
		self.home.client_queue.put(data)

	def sendToWork(self, data):
		self.transport.write(data)
		self.home.work_queue.get().addCallback(self.sendToWork)

#======================================================================
class DataConnToWorkFactory(ClientFactory):
	def __init__(self, home):
		self.home = home

	def buildProtocol(self, addr):
		return DataConnToWork(addr, self.home)

#======================================================================
class ConnToClient(LineReceiver):
	def __init__(self, addr, home):
		self.addr = addr
		self.home = home

	def connectionMade(self):
		print 'Connection received from CLIENT'
		# Add callback then connect to the work server
		self.home.work_queue.put('Connect now')
		self.home.client_queue.get().addCallback(self.sendToClient)

	def connectionLost(self, reason):
		print 'Connection lost from CLIENT'

	def dataReceived(self, data):
		"""Data received from client connection, forward to work"""
		self.home.work_queue.put(data)

	def sendToClient(self, data):
		print 'Sending data to CLIENT'
		self.sendLine(data)
		self.home.client_queue.get().addCallback(self.sendToClient)

#======================================================================
class ConnToClientFactory(ClientFactory):
	def __init__(self, home):
		self.home = home

	def buildProtocol(self, addr):
		return ConnToClient(addr, self.home)

if __name__ == '__main__':
	home = Home()
	home.listen()
