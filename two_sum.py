# hashmap 52.25%
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        index_d = {}
        
        for index, n in enumerate(nums):
            index_d[n] = index
        
        for index, n in enumerate(nums):
            try:
                if index_d[target-n] != index:
                    return [index, index_d[target-n]]
            except KeyError:
                continue