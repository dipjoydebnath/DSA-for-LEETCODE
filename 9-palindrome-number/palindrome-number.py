class Solution(object):
    # the other problem solved here 
    
    def isPalindrome(self, x):
        s = str(x)
        if s == s[::-1]:
            return True
        else:
            return False