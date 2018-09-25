# 54.62%
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_d = {}
        for i in nums:
            count_d[i] = count_d.get(i, 0) + 1
        for i, count in count_d.items():
            if count > len(nums)/2:
                return i