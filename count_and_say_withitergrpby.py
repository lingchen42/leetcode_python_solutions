from itertools import groupby
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        count_seq = "1"
        for num in range(1, n):    
            grps = [list(g) for _, g in groupby(count_seq)]
            count_seq = ["%s%s"%(len(g), g[0]) for g in grps]
            count_seq = "".join(count_seq)
                
        return count_seq