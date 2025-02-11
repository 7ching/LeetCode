class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reach = 0
        for step in range(len(nums)):
            if max_reach < step:
                return False
            max_reach = max(max_reach, step + nums[step])
        return True

nums =[3,2,1,0,4]
print(Solution().canJump(nums))  # Output: True