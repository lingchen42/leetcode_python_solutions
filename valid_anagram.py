# 18.31%
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        count_s = {}
        for c in s:
            count = count_s.get(c, 0) + 1
            count_s[c] = count
            
        count_t = {}
        for c in t:
            count = count_t.get(c, 0) + 1
            count_t[c] = count
            
        if count_s == count_t:
            return True
        else:
            return False