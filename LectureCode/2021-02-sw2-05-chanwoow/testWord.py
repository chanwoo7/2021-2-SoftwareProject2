import unittest
from word import Word


class TestWord(unittest.TestCase):

    def setUp(self):
        self.w1 = Word('words.txt')

    def testRandFromDB(self):
        self.assertTrue(len(self.w1.randFromDB(20)) >= len("abcdefghijklmnopqrst"))
        self.assertTrue(len(self.w1.randFromDB(15)) >= len("abcdefghijklmno"))
        self.assertTrue(len(self.w1.randFromDB(10)) >= len("abcdefghij"))
        self.assertTrue(len(self.w1.randFromDB(5)) >= len("abcde"))
        self.assertEqual(self.w1.randFromDB(21), max(self.w1.words, key=len))
        self.assertEqual(self.w1.randFromDB(1000), max(self.w1.words, key=len))


if __name__ == '__main__':
    unittest.main()