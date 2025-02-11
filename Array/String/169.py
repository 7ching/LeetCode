class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)//2]
    
nums = [1,1,2,4,5,7,3,4,2,2]
print(Solution().majorityElement(nums))  # Output: 3