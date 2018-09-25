class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        
        cur_sum = max_sum = nums[0]
        for num in nums[1:]:
            # if previous cumulative sum is negative, 
            # restart with current number
            cur_sum = max(num, num+cur_sum)
            max_sum = max(max_sum, cur_sum)
        return max_sum