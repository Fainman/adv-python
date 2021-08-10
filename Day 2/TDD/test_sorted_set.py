import unittest
from sorted_set import SortedSet


class TestConstructor(unittest.TestCase):
    def test_empty(self):
        s = SortedSet()

    def test_sequence(self):
        s = SortedSet([7, 8, 3, 1])

    def test_duplicates(self):
        s = SortedSet([8, 8, 8, 8])

    def test_from_iterable(self):
        g = (x for x in range(5))
        s = SortedSet(g)


class TestContainerProtocol(unittest.TestCase):
    def setUp(self):
        self.s = SortedSet([6, 7, 3, 9])

    def test_positive_contained(self):
        self.assertTrue(6 in self.s)

    def test_negative_contained(self):
        self.assertFalse(2 in self.s)

    def test_negative_not_contained(self):
        self.assertTrue(5 not in self.s)

    def test_positive_not_contained(self):
        self.assertTrue(9 in self.s)


class TestSizeProtocol(unittest.TestCase):
    def test_empty(self):
        s = SortedSet()
        self.assertEqual(len(s), 0)

    def test_one(self):
        s = SortedSet([1])
        self.assertEqual(len(s), 1)

    def test_10(self):
        s = SortedSet(range(10))
        self.assertEqual(len(s), 10)

    def test_with_duplicates(self):
        s = SortedSet([5, 5, 5])
        self.assertEqual(len(s), 1)


if __name__ == '__main__':
    unittest.main()
