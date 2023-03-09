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

