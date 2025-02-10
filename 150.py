class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(len(s)-1, -1 ,-1):
            if s[i] ==' ':
                if count == 0:
                    continue
                break
            count += 1 
        return count
        # ----- optimized -----
        # words = s.split()
        # if not words:
        #     return 0
        # return len(words[-1])

        
s = "Hello World"
print(Solution().lengthOfLastWord(s))  # Output: 5