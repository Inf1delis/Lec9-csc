from task2.main import app
import unittest
import requests
import random


class BasicTests(unittest.TestCase):

    _k = '2'
    _value = '{"k":"v"}'

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False

        self.app = app.test_client()
        self.assertEqual(app.debug, False)


    def tearDown(self):
        pass

    def test_delete_returns204(self):
        response = self.app.delete('/cache/1', follow_redirects=True)
        self.assertEqual(response.status_code, 204)

    def test_full_flow(self):
        key = self._k
        value = self._value

        response = self.app.get('/cache/' + key, follow_redirect=True)
        self.assertEqual(response.status_code, 404)

        response = self.app.put('/cache/' + key, data=value, follow_redirect=True)
        self.assertEqual(response.status_code, 201)

        response = self.app.get('/cache/' + key, follow_redirect=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(value, str(response.get_data().decode("utf-8").strip()))

        response = self.app.delete('/cache/' + key, follow_redirect=True)
        self.assertEqual(response.status_code, 204)

        response = self.app.get('/cache/' + key, follow_redirect=True)
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
