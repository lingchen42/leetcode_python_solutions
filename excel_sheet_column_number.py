# 50.34%
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        letter2num_d = {}
        for i in range(65, 91):  # ascii for A-Z
            letter2num_d[chr(i)] = i - 64
            
        out = 0
        for idx, letter in enumerate(s):
            out += 26 ** (len(s) - idx - 1) * letter2num_d[letter]
        
        return out