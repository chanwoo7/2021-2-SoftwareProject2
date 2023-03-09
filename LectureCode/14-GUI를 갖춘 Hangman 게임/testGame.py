import unittest
from game import HangmanGame


class TestHangmanGame(unittest.TestCase):

    def setUp(self):
        self.h1 = HangmanGame()

    def testStartGame(self):
        self.h1.startGame()
        self.assertEqual(self.h1., "e n")
        # self.

if __name__ == '__main__':
    unittest.main()