class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        my_diff = 0
        for i in range(len(prices)): 
            for j in range(i, len(prices)):
                diff = prices[j] - prices[i]
                my_diff = max(my_diff, diff)
        
        return my_diff