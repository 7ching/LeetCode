class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        parts = path.split('/') # split the path by '/'
        for part in parts:
            if part == '' or part == '.':
                continue
            if part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return '/' + '/'.join(stack)


path = "/.../a/../b/c/../d/./"
print(Solution().simplifyPath(path))  # Output: "/home/user/Pictures"