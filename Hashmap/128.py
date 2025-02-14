class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # ----- O(n^2) ----- #
        # long = 0    # consider nums = []
        # for i in nums:
        #     if i-1 not in nums:
        #         j = i
        #         while j in nums:
        #             j += 1
        #             long = max(long, j-i)
        # return long

        # ----- O(n) ----- #
        if not nums:
            return 0
        num_set = set(nums) # set is faster than list
        long = 0
        for i in num_set:   #find the start
            if i-1 not in num_set:
                j = i
                while j in num_set:
                    j += 1
                long = max(long, j-i)
        return long


nums = [100, 4, 200, 1, 3, 2]
print(Solution().longestConsecutive(nums))  # Output: 9