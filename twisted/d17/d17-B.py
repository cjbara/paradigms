from twisted.internet.protocol import Factory
from twisted.internet.protocol import Protocol
from twisted.protocols.basic import LineReceiver
from twisted.internet.tcp import Port
from twisted.internet import reactor

server_host = 'student00.cse.nd.edu'
server_port = 40062

class MyConnection(LineReceiver):

	def __init__(self, addr):
		self.addr = addr
		self.delimeter = "|"

	def connectionMade(self):
		print 'Connection received from '+str(self.addr)

	def dataReceived(self, line):
		print 'Received data: ', line

	def connectionLost(self, reason):
		print 'Connection lost from '+str(self.addr)
		reactor.stop()

class MyConnFactory(Factory):
	def buildProtocol(self, addr):
		return MyConnection(addr)

if __name__ == '__main__':
	reactor.listenTCP(server_port, MyConnFactory())
	reactor.run()
