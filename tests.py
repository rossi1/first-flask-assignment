import unittest
from app import app


class RequestsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(
            response.get_data(as_text=True), 'Hello World',
            "/ should return 'Hello World'")

    def test_python_view(self):
        response = self.app.get('/python')
        data = response.get_data(as_text=True)
        self.assertTrue(
            '<html>' in data,
            "/python should contain an HTML opening tag")

        self.assertTrue(
            '<h1>Python Programming Language</h1>' in data,
            "/python should return 'Python Programming Language as a title'")
