class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        i = 0
        result = []
        while i < len(nums):
            start = nums[i]
            end = nums[i]

            while i+1 < len(nums) and nums[i+1] == nums[i]+1:
                end = nums[i+1]
                i += 1
            i += 1
            if start != end and start < end:
                result.append("{}->{}".format(start, end))
            else:
                result.append(str(start))
        return result
        

nums = [0,2,3,4,6,8,9]
print(Solution().summaryRanges(nums))  # Output: ["0->2","4->5","7"]