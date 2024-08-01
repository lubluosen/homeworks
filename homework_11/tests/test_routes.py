import unittest
from my_flask_app import create_app
from my_flask_app.routes import bp


class RoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.register_blueprint(bp)
        self.client = self.app.test_client()

    def test_contacts(self):
        response = self.client.get('/contacts')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Contacts app.'})


if __name__ == '__main__':
    unittest.main()
