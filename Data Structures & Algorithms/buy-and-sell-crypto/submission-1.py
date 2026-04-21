class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxProfit = 0

        buyp = 2147483647

        for price in prices:
            if price < buyp:
                buyp = price
        
            profit = price - buyp
            maxProfit = max(maxProfit, profit)
        
        return maxProfit
            
