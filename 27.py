class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        p = len(nums) - 1
        while p >= 0:
            if nums[p] == val:
                nums.pop(p)
            p -= 1
        return len(nums)
  

nums = [0, 1, 2, 2, 3, 0, 4, 2]  # Input array
val = 2  # Value to remove
expectedNums = [0, 1, 4, 0, 3]  # The expected answer with correct length.
                                # It is sorted with no values equaling val.

solution = Solution()
k = solution.removeElement(nums, val)  # Calls your implementation

print(k)