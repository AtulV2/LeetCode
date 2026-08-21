class Solution(object):
    def lengthOfLastWord(self, s):
        length = 0

        s = s.rstrip(" ")

        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                length += 1
            else:
                return length

        return length