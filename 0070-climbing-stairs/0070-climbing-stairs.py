import math

class Solution(object):
    def climbStairs(self, n):
        if n == 0:
            return 1
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            temp = [0] * (n + 1) # from 0 to number n total required cells n+1
            temp[0] = 1 # for 0 staircase only 1 way take no step
            temp[1] = 1 # for 1 staricase only 1 way take 1 climb 1
            temp[2] = 2 # for 2 staricase two ways climb 1 + 1 or climb 2 directly 
            
            # for n staricase = n-1 staircase + n-2 staircase ways
            for i in range(3,n+1):
                temp[i] = temp[i-1] + temp[i-2]

            return temp[n]



        