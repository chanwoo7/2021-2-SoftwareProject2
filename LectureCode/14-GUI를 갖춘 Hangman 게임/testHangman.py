import unittest
from hangman import Hangman


class TestHangman(unittest.TestCase):

    def setUp(self):
        self.h1 = Hangman()

    def testGetRemainingLives(self):
        self.assertEqual(self.h1.getRemainingLives(), 6)

    def testDecreaseLife(self):
        self.h1.decreaseLife()
        self.assertEqual(self.h1.getRemainingLives(), 5)
        self.h1.decreaseLife()
        self.h1.decreaseLife()
        self.assertEqual(self.h1.getRemainingLives(), 3)
        self.h1.decreaseLife()
        self.h1.decreaseLife()
        self.h1.decreaseLife()
        self.assertEqual(self.h1.getRemainingLives(), 0)

    def testCurrentShape(self):
        self.assertEqual(self.h1.currentShape(), '''\
   ____
  |    |
  |
  |
  |
  |
 _|_
|   |______
|          |
|__________|\
''')
        self.h1.decreaseLife()
        self.h1.decreaseLife()
        self.assertEqual(self.h1.currentShape(), '''\
   ____
  |    |
  |    o
  |    |
  |    |
  |
 _|_
|   |______
|          |
|__________|\
''')
        self.h1.decreaseLife()
        self.h1.decreaseLife()
        self.h1.decreaseLife()
        self.h1.decreaseLife()
        self.assertEqual(self.h1.currentShape(), '''\
   ____
  |    |
  |    o
  |   /|\\
  |    |
  |   / \\
 _|_
|   |______
|          |
|__________|\
''')

if __name__ == '__main__':
    unittest.main()