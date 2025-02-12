class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = {}
        if len(s) != len(t):
            return False

        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1

        for char in t:
            if char in s_dict:
                s_dict[char] -= 1
                if s_dict[char] == 0:
                    del s_dict[char]
            else:
                return False
        return True

s = "anagram"
t = "nagaram"
print(Solution().isAnagram(s, t))  # Output: True