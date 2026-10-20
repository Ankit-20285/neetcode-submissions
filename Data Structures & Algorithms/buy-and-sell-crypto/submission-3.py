class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0 
        low = float('inf')
        profit = float('-inf')

        for price in prices: 
            low = min(low, price)
            profit = max(profit, price - low)
        
        return profit