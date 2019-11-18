import unittest
import random
import string


def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(stringLength))


class TestStringMethods(unittest.TestCase):

    def test_repeat_elements(self):
        s_random = randomString(random.randint(1, 10))
        set1 = set(s_random)
        set2 = set(s_random*2)
        self.assertEqual(set1, set2)

    def test_add(self):
        set1 = set('hello')
        set2 = set('hello').add('1')
        self.assertNotEqual(set1, set2)

    def test_not_indexing(self):
        set1 = set('hello')
        with self.assertRaises(TypeError):
            set1[:2]

    def test_clear(self):
        set1 = set('12345')
        set1.clear()
        self.assertEqual(len(set1), 0)

    def test_pop(self):
        s = randomString(random.randint(0, 10))
        set1 = set(s)
        poped = set1.pop()
        self.assertEqual(set1, {ch for ch in s if ch != poped})
        set1.clear()
        with self.assertRaises(KeyError):
            set1.pop()

    def test_union(self):
        s1 = randomString(random.randint(1, 10))
        s2 = randomString(random.randint(1, 10))
        set1, set2 = set(s1), set(s2)
        self.assertEqual(set1.union(set2), set(s1+s2))

if __name__ == '__main__':
    unittest.main()
