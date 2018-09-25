# 11.95%
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        out = []
        for i in range(numRows):
            if i == 0:
                t = [1]
                out.append(t)
            elif i == 1:
                t = [1, 1]
                out.append(t)
            else:
                t = []
                t_prev = out[i-1]
                for i, v in enumerate(t_prev[:-1]):
                    t.append(v + t_prev[i+1])
                t = [1] + t + [1]
                out.append(t)
        return out