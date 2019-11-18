from task2.storage import Storage
import unittest
from unittest import mock
import random


class BasicTests(unittest.TestCase):

    def setUp(self):
        self.redis = mock.MagicMock()
        self.table = mock.MagicMock()
        self.storage = Storage(self.redis, self.table)

    def tearDown(self):
        pass

    def test_remove_from_cache(self):
        key = random.randint(1,10)

        self.storage.delete(key)

        self.redis.delete.assert_called_with(key)

    def test_remove_from_mongo(self):
        key = random.randint(1, 10)

        self.storage.delete(key)

        self.table.delete_many.assert_called_with({"key": key})

    def test_get_takes_from_cache(self):
        key = random.randint(1, 10)

        self.redis.exists.return_value = True

        self.storage.get(key)

        self.redis.get.assert_called_with(key)

    def test_get_takes_from_mongo(self):
        key = random.randint(1, 10)

        self.redis.exists.return_value = False

        self.storage.get(key)

        self.table.find_one.assert_called_with({"key": key})

    def test_put_mongo(self):
        key = random.randint(1, 10)

        self.storage.put(key, key)

        self.table.find_one.assert_called_with({"key": key})


if __name__ == '__main__':
    unittest.main()
