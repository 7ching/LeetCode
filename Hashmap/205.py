class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = {}
        if len(s) != len(t):
            return False
        for index in range(len(s)):
            if s[index] in s_dict:
                if s_dict[s[index]] != t[index]:
                    return False
            else:
                if t[index] in s_dict.values():
                    return False
                s_dict[s[index]] = t[index]
        return True

s = "wafhroi"
t = "awfhhow"
print(Solution().isIsomorphic(s, t))  # Output: True