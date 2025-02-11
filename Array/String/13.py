class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict  ={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        result = 0
        pre_value = 0

        for i in range (len(s)-1, -1, -1):
            value = roman_dict[s[i]]
            if value < pre_value:
                result -= value
            else:
                result += value
                pre_value = value
        return result

s = "XMVII"
print(Solution().romanToInt(s))  # Output: 3