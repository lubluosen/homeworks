import unittest
from my_flask_app import create_app


class InitTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Hello, World!'})

    def test_contacts(self):
        response = self.client.get('/contacts')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Contacts app.'})


if __name__ == '__main__':
    unittest.main()
