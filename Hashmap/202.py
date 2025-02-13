class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def cal_sum(n):
            square_sum = 0
            while n > 0:
                square_sum += (n % 10) ** 2
                n = n // 10
            print(square_sum)
            return square_sum
        
        while n >= 10:
            n = cal_sum(n)
        return n == 1


n = 10
print(Solution().isHappy(n))  # Output: True