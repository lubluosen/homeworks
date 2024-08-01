import unittest
import pytest
from my_flask_app import create_app
from my_flask_app.app import add
from my_flask_app.app import subtract
from my_flask_app.app import multiply
from my_flask_app.app import divide


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    rv = client.get('/')
    json_data = rv.get_json()
    assert json_data['message'] == "Hello, World!"


class AppTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(divide(6, 2), 3)
        with self.assertRaises(ValueError):
            divide(1, 0)


if __name__ == '__main__':
    unittest.main()
