# 87.80%
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        uniq_cs = []
        for c in set(list(s)):
            if s.count(c) == 1:
                uniq_cs.append(c)
        for i, c in enumerate(s):
            if c in uniq_cs:
                return i
        return -1