# 52.65%
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        non_zero_idx = 0
        for i in nums:
            if i!=0:
                nums[non_zero_idx] = i
                non_zero_idx += 1
        for i in range(non_zero_idx, len(nums)):
            nums[i] = 0       