import unittest

from google.appengine.ext import ndb
from google.appengine.ext import testbed
from models import Task


class DatastoreTestCase(unittest.TestCase):

    def setUp(self):
        # First, create an instance of the Testbed class.
        self.testbed = testbed.Testbed()
        # Then activate the testbed, which prepares the service stubs for use.
        self.testbed.activate()
        # Next, declare which service stubs you want to use.
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()
        # Clear ndb's in-context cache between tests.
        # This prevents data from leaking between tests.
        # Alternatively, you could disable caching by
        # using ndb.get_context().set_cache_policy(False)
        ndb.get_context().clear_cache()

    def tearDown(self):
        self.testbed.deactivate()

    def testInsertEntity(self):

        # Save Entity
        t = Task()
        t.description = "Hello World"
        t.completed = True
        t.put()

        # Retrieve Entity
        database_task = Task.query().fetch(20)

        # Test retrieved entity
        self.assertEqual(1, len(database_task))
        self.assertEqual(True, database_task[0].completed)
        self.assertEqual("Hello World", database_task[0].description)

if __name__ == '__main__':
        unittest.main()

