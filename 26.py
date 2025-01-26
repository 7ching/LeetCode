class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for p1 in range(len(nums)):
            p2 = p1 + 1
            while p2 < len(nums):
                if nums[p1] == nums[p2]:
                    nums.pop(p2)
                else:
                    p2 += 1
        print(nums)
        return len(nums)

nums = [0,0,1,1,1,2,2,3,3,4]  # Input array
solution = Solution()
k = solution.removeDuplicates(nums) 
print(k)  