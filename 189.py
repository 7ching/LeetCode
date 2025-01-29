class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Time limit exceeded
        # for i in range(k):
        #     nums.insert(0, nums.pop())

        k = k % len(nums)  # 3 % 7 = 3
        nums[:] = nums[-k:] + nums[:-k]  # nums[-3:] + nums[:-3]
        return nums

nums = [1,2,3,4,5,6,7]
k = 3
print(Solution().rotate(nums, k))