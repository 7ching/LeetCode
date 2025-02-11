class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]    # prefix = first string
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:    # if prefix is not found at the beginning of the string
                prefix = prefix[:-1]   # remove the last character (prefix)
                if not prefix:
                    return ""
        return prefix

    
strs = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(strs))  # Output: "fl"