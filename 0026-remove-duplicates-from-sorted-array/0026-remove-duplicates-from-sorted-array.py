class Solution(object):
    def removeDuplicates(self, nums):
        p1 = 0
        p2 = 1
        for i in range(1, len(nums)):
            if nums[p1] == nums[p2]:
                p2 += 1
            else:
                nums[p1 + 1] = nums[p2]
                p1 += 1
                p2 += 1
        
        for i in range(p1,len(nums)-1):
            nums.pop()
        
       

            
        