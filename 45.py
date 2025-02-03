class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_reach = 0
        jump = 0
        current_end = 0

        for step in range(len(nums)-1):
            max_reach = max(max_reach, step + nums[step])
            if  step == current_end:
                jump += 1
                current_end = max_reach
        return jump

nums = [2,3,1,1,4]
print(Solution().jump(nums))  # Output: 2