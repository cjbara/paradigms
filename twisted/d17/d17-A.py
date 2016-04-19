from twisted.internet.protocol import ClientFactory
from twisted.internet.protocol import Protocol
from twisted.internet import reactor

server_host = 'student00.cse.nd.edu'
server_port = 40062

class ClientConnection(Protocol):
	def dataReceived(self, data):
		print 'Received data: ',data

	def connectionMade(self):
		print 'New connection made to '+server_host+' port '+str(server_port)
		data = 'GET /movies/32 HTTP/1.0\r\n\r\n'
		self.transport.write(data)
		self.transport.loseConnection()

	def connectionLost(self, reason):
		print 'Lost connection to '+server_host+' port '+str(server_port)
		reactor.stop()

class ClientConnFactory(ClientFactory):
	def buildProtocol(self, addr):
		return ClientConnection()

if __name__ == '__main__':
	reactor.connectTCP(server_host, server_port, ClientConnFactory())
	reactor.run()
