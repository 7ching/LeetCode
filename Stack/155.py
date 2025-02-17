class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = []   # get minimum in O(1)

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.min or val <=self.min[-1]:
            self.min.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        if self.stack[-1] == self.min[-1]:
            self.min.pop()
        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]
        



# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-3)
obj.push(-2)
obj.push(0)
print(obj.getMin())  # 輸出: -3
obj.pop()
print(obj.top())     # 輸出: -2
print(obj.getMin())  # 輸出: -3