class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = 2
        while p <= len(nums)-1:
            if nums[p] == nums[p-1] & nums[p] == nums[p-2]:
                nums.pop(p)
                p -= 1
            p += 1
        print(nums)
        return len(nums)
    
nums = [0,0,1,1,1,1,2,3,3]
print(Solution().removeDuplicates(nums))