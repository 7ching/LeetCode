class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine_dict = {}

        for i in magazine:
            if i in magazine_dict:
                magazine_dict[i] += 1
            else:
                magazine_dict[i] = 1
        
        for i in ransomNote:
            if i in magazine_dict:
                magazine_dict[i] -= 1
                if magazine_dict[i] == 0:
                    del magazine_dict[i]
            else:
                return False
        return True
ransomNote = "aa"
magazine = "aab"
print(Solution().canConstruct(ransomNote, magazine))  # Output: True