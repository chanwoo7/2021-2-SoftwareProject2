import unittest

from palindrome import Palindrome

class TestPalindrome(unittest.TestCase):

    def setUp(self):
        self.p1 = Palindrome('abcd')
        self.p2 = Palindrome('abcdedcba')
        self.p3 = Palindrome('ab c d cba')
    
    def tearDown(self):
        pass
    
    def testNormal(self):
        self.assertFalse(self.p1.normal())
        self.assertTrue(self.p2.normal())
        self.assertFalse(self.p3.normal())
    
    def testRecursive(self):
        self.assertFalse(self.p1.recursive())
        self.assertTrue(self.p2.recursive())
        self.assertFalse(self.p3.recursive())
    
    def testIgnoreSpaces(self):
        self.assertFalse(self.p1.ignoreSpaces())
        self.assertTrue(self.p2.ignoreSpaces())
        self.assertTrue(self.p3.ignoreSpaces())

if __name__ == '__main__':
    unittest.main()

