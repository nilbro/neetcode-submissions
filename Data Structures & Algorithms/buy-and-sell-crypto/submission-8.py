class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(len(prices)-1):
            buy_price = prices[i]
            sell_price = max(prices[i+1:])
            profit = sell_price - buy_price
            maxProfit = max(profit, maxProfit)
        return maxProfit