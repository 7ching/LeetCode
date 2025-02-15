class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # ----- optimized ----- #
        stack = []
        hash = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in hash.values():
                stack.append(c)
            elif c in hash:
                if not stack or stack.pop() != hash[c]:
                    return False
        return not stack

        # stack = []
        # for c in s:
        #     if c in set(['(', '[', '{']):
        #         stack.append(c)
        #     else:
        #         if c == ')':
        #             if not stack or stack.pop() != '(':
        #                 return False
        #         elif c == ']':
        #             if not stack or stack.pop() != '[':
        #                 return False
        #         elif c == '}':
        #             if not stack or stack.pop() != '{':
        #                 return False
        # return not stack

s = "([])"
print(Solution().isValid(s))  # Output: True