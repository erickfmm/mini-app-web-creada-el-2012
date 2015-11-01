import os
import webapp2
import jinja2
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

class Entries(db.Model):
	subject = db.StringProperty(required = True)
	content = db.TextProperty(required = True)
	created = db.DateTimeProperty(auto_now_add = True)
	identification=db.IntegerProperty()

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class Blog1(Handler):
	def get(self):
		entries = db.GqlQuery("SELECT * FROM Entries ORDER BY created DESC")
		self.render("index.html", entries=entries)
	
class Newpost(Handler):
	def render_new(self, subject="", content="", error=""):
		self.render("Newpost.html", subject=subject, content=content, error = error)
	def get(self):
		self.render_new()
	def post(self):
		subject = self.request.get("subject")
		content = self.request.get("content")
		if subject and content:
			entry=Entries(subject=subject, content=content)
			key=entry.put()
			entry.identification = int(key.id())
			entry.put()
			self.redirect("/blog1/%d" % key.id())
		else:
			error = "ingresa subject y content"
			self.render_new(subject=subject, content=content, error=error)
			
class Permalink(Handler):
	def get(self, post_id):
		post=Entries.get_by_id(int(post_id))
		subject=post.subject
		content=post.content
		self.render("Permalink.html", subject=subject, content=content)

