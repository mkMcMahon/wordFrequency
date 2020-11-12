import unittest

from main2 import wordSorter


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertIsNone(wordSorter())


if __name__ == '__main__':
    unittest.main()
