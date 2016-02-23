#!/usr/bin/env python
#

import webapp2
import init
from models import Task

# code to init
init.init_db()


class MainHandler(webapp2.RequestHandler):
    def get(self):
        tasks = Task.query().order(Task.date_created).fetch(20)
        self.response.headers['Content-Type'] = 'text/plain'
        for t in tasks:
            self.response.write("------------------------------------------\n")
            self.response.write("Task Description: " + t.description + "\n")
            self.response.write("Date Created: " + str(t.date_created) + "\n")
            self.response.write("------------------------------------------\n")

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)


