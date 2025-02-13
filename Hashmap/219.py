class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # ----- O(n^2) ----- #
        # p2 = len(nums) - 1

        # while p2 >=0:
        #     for p1 in range(p2):
        #         if nums[p1] == nums[p2] and abs(p1 - p2) <= k:
        #             return True
        #     p2 -= 1
        # return False

        # ----- O(n) ----- #
        num_to_index = {}
        for i, num in enumerate(nums):
            if num in num_to_index and abs(num_to_index[num] - i) <= k:
                    return True
            else:
                num_to_index[num] = i
        return False


        
nums = [1,2,3,1,2,1]
k = 2
print(Solution().containsNearbyDuplicate(nums, k))  # Output: False