class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # if haystack.find(needle) == -1:
        #     return -1
        # for i in range(len(haystack)):
        #     if haystack[i:i+len(needle)] == needle:
        #         return i
        return haystack.find(needle)    # .find() : returns the index of the first occurrence of the substring (-1 if not found)
haystack = "sadbutsad"
needle = "sad"
print(Solution().strStr(haystack, needle))  # Output: 0