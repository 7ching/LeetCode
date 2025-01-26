class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_profit = 0

        for now in prices:
            min_price = min(min_price, now)
            max_profit = max(max_profit, now - min_price)
        return max_profit
    
prices = [7,6,4,3,1]
print(Solution().maxProfit(prices))  # Output: 5