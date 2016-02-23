from google.appengine.ext import ndb


class Task(ndb.Model):
    description = ndb.StringProperty()
    completed = ndb.BooleanProperty(required=True, default=False)
    date_created = ndb.DateTimeProperty(auto_now_add=True, required=True)
    date_modified = ndb.DateTimeProperty(auto_now=True, required=True)


