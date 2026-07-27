class Solution(object):
    def removeElement(self, nums, val):

        # here k is our pointer

        k = 0
        for i in range(0, len(nums)):
            if nums[i] == val:
                continue
            
            else:
                nums[k] = nums[i]
                k = k + 1
            
        return k





        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        