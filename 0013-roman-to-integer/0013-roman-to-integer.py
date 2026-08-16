class Solution(object):
    def romanToInt(self, s):
        map = {
            "I"       :      1,
            "V"       :      5,
            "X"       :      10,
            "L"       :      50,
            "C"       :     100,
            "D"       :      500,
            "M"       :     1000
        }

        hasmap = {}
        for i in s:
           
           if i in hasmap:
             hasmap[i] += 1
           else:
            hasmap[i] = 1

        intnum = 0
        for i in hasmap:
                temp = map[i]
                intnum += temp * hasmap[i]

        if ("IV" in s) or ("IX" in s):
            intnum -= 2


        if ("XL" in s) or ("XC" in s):
            intnum -= 20


        if ("CD" in s) or ("CM" in s):
            intnum -= 200

        

        return intnum


        



        

        