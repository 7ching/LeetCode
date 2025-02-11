class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [1] * len(nums)
        right = [1] * len(nums)
        result = [1] * len(nums)

        for i in range(1, len(nums)):   # i=2, num=3
            left[i] = left[i-1] * nums[i-1]  # left[2] = (1*5) * 7 = 35
        for i in range(len(nums)-2, -1, -1):               
            right[i] = right[i+1] * nums[i+1]   # right[2] = 1 * 8 = 8
        for i in range(len(nums)):
            result[i] = left[i] *right[i]  # result[2] = 35 * 8 = 280
        return result
        
nums = [5,7,3,8]
print(Solution().productExceptSelf(nums))  # Output: [168, 120, 280, 105]

# left = [1, 5, 35, 105]
# right = [168, 24, 8, 1]