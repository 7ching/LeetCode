class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        for today in range(1, len(prices)):
            if prices[today] > prices[today-1]:
                max_profit += prices[today] - prices[today-1]
                print(max_profit,"=" ,prices[today], "-", prices[today-1])
        return max_profit
    
prices = [7, 1, 5, 3, 4, 6]
solution = Solution()
print(solution.maxProfit(prices)) 