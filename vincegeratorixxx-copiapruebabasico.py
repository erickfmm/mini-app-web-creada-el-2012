#print 'Content-Type: text/plain'
#print ''
#print 'Hello, Udacity'

import webapp2
#from google.appengine.ext import webapp
#from google.appengine.ext.webapp.util import run_wsgi_app

form = """
<form action="/testform">
    <input name="q"> <input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
   def get(self):
      #self.response.headers['Content-Type'] = 'text/html'
      self.response.out.write(form)
        
class TestHandler(webapp2.RequestHandler):
   def get(self):
      #q=self.request.get("q")
      #self.response.out.write(q)
      
      self.response.headers['Content-Type'] = 'text/plain'
      self.response.out.write(self.request)

app = webapp2.WSGIApplication([('/', MainPage), 
				('/testform', TestHandler)], 
				debug=True)
				
