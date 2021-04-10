import unittest
from RedBlackTree import RedBlackTree
from random import randint


class TestRBT(unittest.TestCase):
    def setUp(self):
        self.rbt = RedBlackTree()

    def tearDown(self):
        self.rbt.clear()

    def test_search_in_empty(self):
        self.assertFalse(self.rbt.search(1))

    def test_insert_search_one_number(self):
        self.rbt.insert(10)
        self.assertTrue(self.rbt.search(10))
        self.assertFalse(self.rbt.search(1))

    def test_stress_mode(self):
        s = set()
        SIZE = 10000
        for i in range(SIZE):
            x = randint(0, SIZE)
            self.rbt.insert(x)
            s.add(x)
        for i in range(SIZE):
            x = randint(0, SIZE)
            self.assertEqual(x in s, self.rbt.search(x))
