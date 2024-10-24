import unittest
from apptest import app

class ContactAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        """Test if the home page loads correctly."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Contacts', response.data)

    def test_add_contact(self):
        """Test adding a new contact via the form."""
        response = self.app.post('/new', data=dict(name='John Doe', phone='123456789'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'John Doe', response.data)
        self.assertIn(b'123456789', response.data)

    def test_duplicate_contact(self):
        """Test adding the same contact twice."""
        self.app.post('/new', data=dict(name='Jane Doe', phone='987654321'), follow_redirects=True)
        response = self.app.post('/new', data=dict(name='Jane Doe', phone='987654321'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Jane Doe', response.data)
        # Optionally, check for a specific message if duplicates should not be allowed

    def test_contact_display(self):
        """Test that all added contacts are displayed on the home page."""
        self.app.post('/new', data=dict(name='John Smith', phone='1122334455'), follow_redirects=True)
        response = self.app.get('/')
        self.assertIn(b'John Smith', response.data)
        self.assertIn(b'1122334455', response.data)


if __name__ == '__main__':
    unittest.main()
