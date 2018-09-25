# 49% can also implement using collecionts.Counter
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums_d = {number: count}
        nums_d = {}
        for i in nums:
            count = nums_d.get(i, 0)
            nums_d[i] = count + 1
            
        # find the uniq number  
        for num, count in nums_d.items():
            if count == 1:
                return num