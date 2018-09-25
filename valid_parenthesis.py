# stack implementation
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {")":"(", "]":"[", "}":"{"}
        # stack
        if not s:
            return True
        
        t = [s[0]]
        for i in s[1:]:
            if i in ["(", "[", "{"]:
                t.append(i)
            else:
                if (len(t) == 0) or d[i] != t.pop():
                    return False
                
        return not stack