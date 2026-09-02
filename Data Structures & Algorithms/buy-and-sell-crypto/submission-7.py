class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        b, s = 0, 1
        while s < len(prices):
            if prices[b] > prices[s]:
                b = s
            else:
                profit = prices[s] - prices[b]
                max_profit = max(profit, max_profit)
            s += 1
        return max_profit