class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash = {}
        for i in range(len(strs)):
            sort_word = ''.join(sorted(strs[i]))    # ''.join() : convert list to string
            if sort_word in hash:
                hash[sort_word].append(strs[i])
            else:
                hash[sort_word] = [strs[i]]
        return list(hash.values())  # convert to list
        
strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs))  # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]