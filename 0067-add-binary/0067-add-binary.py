class Solution(object):
    def addBinary(self, a, b):

        while len(a) != len(b):
            if len(a) > len(b):
                b = "0" + b
            else:
                a = "0" + a

        result = ""
        carry = 0
        i = len(a) - 1

        while i >= 0:
            total = int(a[i]) + int(b[i]) + carry

            result = str(total % 2) + result
            carry = total // 2

            i -= 1

        if carry:
            result = "1" + result

        return result