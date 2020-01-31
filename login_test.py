import unittest
import os
from run import app
import tempfile
import appli
from appli import config

class BasicTestCase(unittest.TestCase):

    def test_index(self):
        """Initial test: Ensure flask was set up correctly."""
        tester = appli.app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_database(self):
        """Initial test: Ensure that the database exists."""
        tester = os.path.exists("app.db")
        self.assertEqual(tester, True)

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        """Set up a blank temp database before each test."""
        self.db_fd, appli.app.config["DATABASE"] = tempfile.mkstemp()
        self.app = appli.app.test_client()
        appli.create_app()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(appli.app.config["DATABASE"])

    def login(self, email, password):
        return self.app.post('/login', data=dict(
            email=email,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def signup(self, name,display_name, email, password):
        return self.app.post('/signup', data=dict(
            name=name,
            display_name=display_name,
            email=email,
            password=password
        ), follow_redirects=True)











if __name__ == '__main__':
    unittest.main()