import unittest
from app import app, registrations


class AppTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()
        registrations.clear()

    def tearDown(self):
        registrations.clear()

    def test_index_page_loads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Event Registration Portal', response.data)

    def test_health_endpoint(self):
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'status': 'ok'})

    def test_registration_with_missing_fields(self):
        response = self.client.post('/', data={'name': '', 'email': '', 'event': ''}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'All fields are required.', response.data)

    def test_successful_registration(self):
        response = self.client.post(
            '/',
            data={'name': 'Test User', 'email': 'test@example.com', 'event': 'DevOps Bootcamp'},
            follow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Successfully registered Test User for DevOps Bootcamp!', response.data)
        self.assertIn(b'Test User', response.data)


if __name__ == '__main__':
    unittest.main()
