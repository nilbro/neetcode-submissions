class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            sell_price = prices[i]
            buy_price = min(prices[:i+1])
            profit = sell_price - buy_price
            max_profit = max(profit, max_profit)
        return max_profit