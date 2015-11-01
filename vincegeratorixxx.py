import webapp2
import Tarea3
import rot13
#import jinja2
#from google.appengine.ext import db
#import os

form = """
<form method="post" action="%(accion)s">
	<label>
		Username
		<input type="text" name="username" value="%(user)s">
		%(error_user)s
	</label>
	<br>
	<label>
		Password
		<input type="text" name="password" value="">
		%(error_pass)s
	</label>
	<br>
	<label>
		Verity Password
		<input type="text" name="verify" value="">
		%(error_verify)s
	</label>
	<br>
	<label>
		Email (optional)
		<input type="text" name="email" value=%(mail)s>
		%(error_email)s
	</label>
	<br>
	<input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
	def get(self):
		#self.response.headers['Content-Type'] = 'text/html'
      
		self.write_form()
	def post(self):
		username=self.request.get("username")
		password=self.request.get("password")
		verify=self.request.get("verify")
		email=self.request.get("email")
		error_user=""
		error_pass=""
		error_verify=""
		error_email=""
		ok=True
		if(username.count(" ") > 0 or not username):
			error_user="That's not a valid username."
			ok=False
		if not(password and verify):
			error_pass="That wasn't a valid password."
			ok=False
		elif((len(password) <=3) or (len(verify) <=3)):
			error_pass="That wasn't a valid password."
			ok=False
		elif(password != verify):
			error_verify="Your passwords didn't match."
			ok=False
		spaces_in_email=email.count(" ")
		arroba=email.find("@")
		if(arroba!= -1): 
			punto=email.find(".", arroba)
		else: 
			punto=0
		despues_punto=email[punto+1:]
		if(spaces_in_email!=0 or arroba==-1 or punto==0 or len(despues_punto)==0):
			error_email="That's not a valid email."
			if email:
				ok=False
		if not ok:
			self.write_form("/", username, error_user, error_pass, error_verify, email, error_email)
		else:
			self.redirect('/welcome?username='+username)
			
      
	def write_form(self, accion="/", user="", error_user="", error_pass="", error_verify="", mail="", error_email=""):
		self.response.out.write(form % {"accion":accion, "user":user, "error_user":error_user, "error_pass":error_pass, "error_verify":error_verify, "mail":mail, "error_email":error_email})
class TestHandler(webapp2.RequestHandler):
	def get(self):
		username=self.request.get('username')
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.out.write("Welcome, "+username+"!")
	def post(self):
		#self.response.get(username)
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.out.write("Welcome, "+self.request.username+"!")

app = webapp2.WSGIApplication([('/', MainPage),
				('/welcome', TestHandler), ('/blog1', Tarea3.Blog1),
				('/blog1/newpost', Tarea3.Newpost), ('/blog1/(\d+)', Tarea3.Permalink),
				('/rot13', rot13.Rot13)], 
				debug=True)
				
