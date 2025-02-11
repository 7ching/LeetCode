class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        p_s = p_t = 0
        if len(t) < len(s):
            return False
        if len(s) == 0:
            return True
        while p_t < len(t):
            if s[p_s].lower() == t[p_t].lower():
                p_s += 1
                if(p_s == len(s)):
                    return True
            p_t += 1
        return False 
        
s = "axc"
t = "ahbgdc"
print(Solution().isSubsequence(s, t))