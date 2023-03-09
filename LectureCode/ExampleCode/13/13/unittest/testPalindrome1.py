import unittest

from palindrome import Palindrome

class TestPalindrome(unittest.TestCase):

    def setUp(self):
        self.p1 = Palindrome('abcd')
        self.p2 = Palindrome('abcdedcba')
    
    def tearDown(self):
        pass
    
    def testNormal(self):
        self.assertFalse(self.p1.normal())
        self.assertTrue(self.p2.normal())

if __name__ == '__main__':
    unittest.main()

