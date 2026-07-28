class Solution(object):
    def searchInsert(self, nums, target):
        
        left = 0
        right = len(nums) - 1

        while left <= right:

            midium_base = (left + right) // 2

            if nums[midium_base] == target:
                return midium_base

            elif target <= nums[midium_base]:
                right = midium_base - 1

            else:
                left = midium_base + 1
        
        return left


        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        