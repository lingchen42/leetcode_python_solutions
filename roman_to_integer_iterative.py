# iterative 43.10%
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = ["I", "V", "X", "L", "C", "D", "M"]
        values = [1, 5, 10, 50, 100, 500, 1000]
        lv = dict(zip(letters, values))
        
        out = 0
        for i, c in enumerate(s[:-1]):
            if lv[c] < lv[s[i+1]]:
                out -= lv[c]
            else:
                out += lv[c]
        out += lv[s[-1]]
        return out