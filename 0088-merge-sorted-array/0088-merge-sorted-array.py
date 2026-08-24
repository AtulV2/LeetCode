class Solution(object):
    def merge(self, nums1, m, nums2, n):
        p1 = m - 1
        p2 = n - 1
        k = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums2[p2] > nums1[p1]:
                nums1[k] = nums2[p2]
                k -= 1
                p2 -= 1
            else: 
                nums1[k] = nums1[p1]
                k -= 1
                p1 -= 1
        

        while p2 >= 0:
            nums1[k] = nums2[p2]
            k -= 1
            p2 -= 1
        return nums1
            


        
