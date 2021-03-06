import webapp2

from responses import toaster
from responses import tutorial


class RootHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')


class ToasterHandler(webapp2.RedirectHandler):
    def get(self):
        self.response.headers.add_header("Access-Control-Allow-Origin", "*")
        self.response.headers["Content-type"] = "application/json"
        self.response.write(toaster.get_response())


class TutorialHandler(webapp2.RedirectHandler):
    def get(self):
        self.response.headers.add_header("Access-Control-Allow-Origin", "*")
        self.response.headers["Content-type"] = "application/json"
        self.response.write(tutorial.get_response())
