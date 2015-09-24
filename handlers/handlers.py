import webapp2
from responses import toaster


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class ToasterHandler(webapp2.RedirectHandler):
    def get(self):
        self.response.write(toaster.get_response())

class TutorialHandler(webapp2.RedirectHandler):
    def get(self):
        self.response.write('Tutorial')
