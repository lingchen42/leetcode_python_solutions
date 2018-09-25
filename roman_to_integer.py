# recurrent solution 17.59%
letters = ["I", "V", "X", "L", "C", "D", "M"]
values = [1, 5, 10, 50, 100, 500, 1000]
lv = dict(zip(letters, values))
combined = ["IV", "IX", "XL", "XC", "CD", "CM"]

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return lv.get(s, 0)
        else:
            # recurrent solution
            if s[:2] in combined:
                return lv[s[1]] - lv[s[0]] + self.romanToInt(s[2:])
            else:
                return lv[s[0]] + self.romanToInt(s[1:])