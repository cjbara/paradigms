import cherrypy
import json

class HelloWorldController(object):
    def __init__(self):
        self.datum = 'Go Irish!'

    def GET(self):
        return 'Hello ' + self.datum

    def POST(self):
        output = {'result': 'success'}
        
        try:
            data = cherrypy.request.body.read()
            processed_data = json.loads(data)
            self.datum = processed_data['thedata']
        except Exception as ex:
            output['result'] = str(ex)
        
        return json.dumps(output)

myHWC = HelloWorldController()

dispatcher = cherrypy.dispatch.RoutesDispatcher()
dispatcher.connect('helloworldget', '/helloworld', controller = myHWC, action = 'GET', conditions = dict(method=['GET']))
dispatcher.connect('helloworldpost', '/helloworld', controller = myHWC, action = 'POST', conditions = dict(method=['POST']))

conf = { 'global': {'server.socket_host': '127.0.0.1', 'server.socket_port': 40085}, '/': {'request.dispatch': dispatcher } }
cherrypy.config.update(conf)
app = cherrypy.tree.mount(None, config = conf)
cherrypy.quickstart(app)
