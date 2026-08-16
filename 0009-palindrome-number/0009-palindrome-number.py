class Solution(object):
    def isPalindrome(self, x):
        temp = x
        revNum = 0
        while x > 0:
            digit = x % 10
            revNum = digit + (revNum * 10)
            x = x // 10
       
        if temp == revNum:
            return True
        else:
            return False
        