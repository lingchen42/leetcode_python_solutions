# 98.45%
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        ss = set()
        while (n != 1) and (n not in ss): 
            ss.add(n)
            s = 0
            for i in str(n):
                s += int(i)**2 
            n = s
            
        if n == 1:
            return True
        else:
            return False