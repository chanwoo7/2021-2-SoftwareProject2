import unittest
from guess import Guess


class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess("default")

    def testGuess(self):
        self.assertTrue(self.g1.guess("d"))
        self.assertTrue(self.g1.guess("t"))
        self.assertTrue(self.g1.guess("e"))
        self.assertTrue(self.g1.guess("a"))
        self.assertTrue(self.g1.guess("u"))
        self.assertFalse(self.g1.guess("1"))
        self.assertFalse(self.g1.guess("w"))
        self.assertFalse(self.g1.guess("q"))
        self.assertFalse(self.g1.guess("/"))
        self.assertFalse(self.g1.guess("'"))

    def testFinished(self):
        self.assertFalse(self.g1.finished())
        self.g1.guess('d')
        self.g1.guess('f')
        self.g1.guess('a')
        self.g1.guess('u')
        self.g1.guess('l')
        self.g1.guess('t')
        self.assertTrue(self.g1.finished())

    def testDisplayCurrent(self):
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.g1.guess('w')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.g1.guess('1')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')

    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
        self.g1.guess('w')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u w ')
        self.g1.guess('1')
        self.assertEqual(self.g1.displayGuessed(), ' 1 a e n t u w ')
        self.g1.guess('/')
        self.assertEqual(self.g1.displayGuessed(), ' / 1 a e n t u w ')


if __name__ == '__main__':
    unittest.main()