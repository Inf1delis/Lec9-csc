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


if __name__ == '__main__':
    unittest.main()
