from twisted.internet.protocol import ClientFactory
from twisted.internet.protocol import Protocol
from twisted.internet import reactor

server_host = 'student02.cse.nd.edu'
server_port = 40001

class ClientConnection(Protocol):
	"""
	This class is a special instance of Protocol that overrides its methods to handle the
	incoming data properly. By overriding these methods, we are able to get the data from the
	server and print it out in a way that works best for our program.
	"""
	def dataReceived(self, data):
		"""
		After we make the connection, we are constantly waiting for incoming data from the server.
		When response data is received, this function is called, and it prints out the data.
		"""
		print 'Received data: ',data

	def connectionMade(self):
		"""
		This function is run as soon as a connection is made with the server.
		This acts as a handler for when the connection is made.
		Once the connection is established, we send the data to the server 
		and then wait for a response.
		"""
		print 'New connection made to '+server_host+' port '+str(server_port)
		data = 'GET /movies/32 HTTP/1.0\r\n\r\n'
		self.transport.write(data)

	def connectionLost(self, reason):
		"""
		This function is the handler for when the connection to the server is lost.
		Once the connection is lost, the Twisted library calls this function to notify 
		the user of the lost connection, at which point we print out the message and stop
		receiving data.
		"""
		print 'Lost connection to '+server_host+' port '+str(server_port)
		reactor.stop()

class ClientConnFactory(ClientFactory):
	"""
	This factory class builds a ClientConnection class and returns it in order to be 
	used later in the program. This is its only job is to properly build a 
	ClientConnection instance.
	"""
	def buildProtocol(self, addr):
		"""
		This function is called when we have to build our particular protocol instance,
		the ClientConnection class, which inherits from protocol.
		This creates the ClientConnection, which Twisted then uses to create connections
		and handle incoming data.
		"""
		return ClientConnection()

if __name__ == '__main__':
	reactor.connectTCP(server_host, server_port, ClientConnFactory())
	reactor.run()
