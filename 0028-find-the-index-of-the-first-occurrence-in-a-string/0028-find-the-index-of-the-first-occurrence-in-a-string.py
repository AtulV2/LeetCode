class Solution(object):
    def strStr(self, haystack, needle):
        if needle == "":
            return 0

        p1 = 0

        while p1 < len(haystack):
            start = p1
            p2 = 0

            while p2 < len(needle) and p1 < len(haystack):
                if haystack[p1] == needle[p2]:
                    p1 += 1
                    p2 += 1
                else:
                    break

            if p2 == len(needle):
                return start

            p1 = start + 1

        return -1


        