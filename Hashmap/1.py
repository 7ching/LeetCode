class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # ----- O(n^2) ----- #
        # for i in range(len(nums)):
        #     diff = target - nums[i]
        #     if (diff) in nums and nums.index(diff) != i:
        #         return [i, nums.index(diff)]
            
        # ----- O(n) ----- #
        num_to_index = {}
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in num_to_index:
                return [num_to_index[diff], i]
            num_to_index[num] = i


nums = [2,7,11,15]
target = 9
print(Solution().twoSum(nums, target))  # Output: [0,1]