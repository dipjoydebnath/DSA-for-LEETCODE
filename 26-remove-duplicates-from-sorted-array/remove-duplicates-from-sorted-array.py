class Solution(object):
    # this is my new streak starts from today
    
    def removeDuplicates(self, nums):
        n=len(nums)
        if n==0:
            return 0
        
        j = 0   # slow pointer
        
        for i in range(0, n):   # fast pointer
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        
        return j + 1