#print 'Content-Type: text/plain'
#print ''
#print 'Hello, Udacity'

import webapp2
#from google.appengine.ext import webapp
#from google.appengine.ext.webapp.util import run_wsgi_app

form = """
<form method="post">
	<textarea name="text"
		style="height: 100px; width: 400px;">%(texto)s</textarea>
	<br>
	<input type="submit">
</form>
"""

class Rot13(webapp2.RequestHandler):
	def get(self):
		#self.response.headers['Content-Type'] = 'text/html'
      
		self.write_form()
	def post(self):
		q=self.request.get("text")
		self.write_form(q.encode("rot13"))
      
	def write_form(self, texto=""):
		self.response.out.write(form % {"texto":texto})
#class TestHandler(webapp2.RequestHandler):
   #def get(self):
      
      
      
      #self.response.headers['Content-Type'] = 'text/plain'
      #self.response.out.write(self.request)

#app = webapp2.WSGIApplication([('/', MainPage)], 
				#debug=True)
				
