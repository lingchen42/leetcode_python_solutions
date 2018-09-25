# 22.05%
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        if len(prices) >= 1:
            for i, p in enumerate(prices[:-1]):
                next_p = prices[i+1]
                diff = next_p - p
                if diff > 0:
                    # buy in or hold
                    max_profit += diff
        return max_profit