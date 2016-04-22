# Cory Jbara
# Twisted Daily 18

from twisted.internet.protocol import Factory
from twisted.internet.protocol import ClientFactory
from twisted.internet.protocol import Protocol
from twisted.protocols.basic import LineReceiver
from twisted.internet.tcp import Port
from twisted.internet import reactor
from twisted.internet.defer import DeferredQueue

my_host = 'student00.cse.nd.edu'
my_port = 40062
server_host = 'student02.cse.nd.edu'
server_port = 40001

#create the queue
queue = DeferredQueue()

class ConnectionToClient(LineReceiver):
	"""This class is the connection from the client. It takes data from the client and launches a connection to the server"""

	def __init__(self, addr, queue):
		"""We need a reference to the queue, and also the address of the client that is connecting."""
		self.addr = addr
		self.queue = queue

	def connectionMade(self):
		"""Until the client asks for a connection, this class just blocks. Once a connection is made, it builds the connection to the server and waits for data"""
		print 'Connection received from '+str(self.addr)
		reactor.connectTCP(server_host, server_port, ConnectionToServerFactory(self.queue, self))

	def dataReceived(self, line):
		"""Once data is received, it puts this data on the queue. The data is popped off when the connection to the server is made"""
		self.queue.put(line)

	def connectionLost(self, reason):
		"""Once the connection is lost, it stops waiting for events"""
		print 'Connection lost from '+str(self.addr)
		reactor.stop()

	def sendToClient(self, data):
		"""The callback for when the proxy gets information back from the server. It takes the data and immediately forwards it to the client"""
		self.sendLine(data)
		self.queue.get().addCallback(self.sendToClient)
	
class ConnectionToClientFactory(Factory):
	"""This class builds a connection to the client once the listenTCP is called""" 
	def __init__(self, queue):
		"""The queue must be passed to all handler classes"""
		self.queue = queue

	def buildProtocol(self, addr):
		"""Builds a connection to the client"""
		return ConnectionToClient(addr, self.queue)

class ConnectionToServer(Protocol):
	"""This class acts as the gateway to the server"""
	def __init__(self, queue, proxy):
		"""In order to create the proper handlers, we have to have a reference to the connection to the client. Also we need a reference to the queue so that we can add and handle events."""
		self.queue = queue
		self.proxy = proxy

	def connectionMade(self):
		"""Once a connection is made to the server, we have to handle the data that we received from the client. We do this with the sendToServer callback. Then we put another callback on the queue, which will handle data once we get it back from the server."""
		print 'Connection made to '+server_host+' port '+str(server_port)
		self.queue.get().addCallback(self.sendToServer)
		self.queue.get().addCallback(self.proxy.sendToClient)

	def dataReceived(self, data):
		"""Once we receive data from the server, we put it on the queue. Since we already put the handler on the queue (proxy.sendToClient), it will be sent back to the client"""
		self.queue.put(data)

	def sendToServer(self, data):
		"""This method takes data from the queue and it sends it to the server"""
		self.transport.write(data)

class ConnectionToServerFactory(ClientFactory):
	"""This is the factory class to build the connection to the server"""
	def __init__(self, queue, proxy):
		"""We need both these references so we can pass them to the ClientConnection we are creating"""
		self.queue = queue
		self.proxy = proxy

	def buildProtocol(self, addr):
		"""This builds the connection with the queue and the proxy references"""
		return ConnectionToServer(self.queue, self.proxy)

if __name__ == '__main__':
	reactor.listenTCP(my_port, ConnectionToClientFactory(queue))
	reactor.run()
