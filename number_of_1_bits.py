# 88%
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        out = 0
        while n > 0:
            r = n%2
            if r: out+=1
            n /= 2
        return out