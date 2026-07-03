class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minLeft, profit = max(prices), 0
        for i in range(len(prices)):
            print(i, minLeft, profit)
            if i > 0 and prices[i-1] < minLeft:
                minLeft = prices[i-1]
            profit = max(prices[i]-minLeft,profit)
        return profit
            
