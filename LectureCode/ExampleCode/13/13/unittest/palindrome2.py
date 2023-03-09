class Palindrome:

    def __init__(self, s):
        self.x = s
    
    def normal(self):
        l = 0; r = len(self.x) - 1
        bPalin = False
        while l < r:
            if self.x[l] != self.x[r]:
                break
            l += 1; r -= 1
        else:
            bPalin = True
        return bPalin

    def recursive(self):
        return self.r(self.x)
    
    def r(self, s):
        if len(s) == 0 or len(s) == 1:
            return True
        return s[0] == s[-1] and self.r(s[1:-1])

