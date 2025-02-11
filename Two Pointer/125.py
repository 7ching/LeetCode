class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p_start = 0
        p_end = len(s) - 1
        while p_start < p_end:
            if not s[p_start].isalnum():
                p_start += 1
            elif not s[p_end].isalnum():
                p_end -= 1
            else:
                if s[p_start].lower() != s[p_end].lower():
                    return False
                p_start += 1
                p_end -= 1
        return True

s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))  # Output: True