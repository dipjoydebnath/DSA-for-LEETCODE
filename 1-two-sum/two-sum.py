class Solution:
    # this is one of the main thing
    
    def twoSum(self,nums,target):
        n = len(nums)
        for j in range(0,n-1):
            for i in range(j+1,n):
                if nums[i] + nums[j]== target:
                    return[j,i]