class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s_list = s.split()
        if len(s_list) != len(pattern):
            return False
        
        pattern_dict = {}
        for index in range(len(pattern)):
            if pattern[index] in pattern_dict:
                if pattern_dict[pattern[index]] != s_list[index]:
                    return False
            else:
                if s_list[index] in pattern_dict.values():
                    return False
                pattern_dict[pattern[index]] = s_list[index]
        return True


pattern = "abba"
s = "dog cat cat dog"
print(Solution().wordPattern(pattern, s))  # Output: True