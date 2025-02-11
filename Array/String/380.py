import random
class RandomizedSet(object):

    def __init__(self):
        self.val = []
        self.index = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.index:
            return False
        self.val.append(val)
        self.index[val] = len(self.val) - 1
        return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.index:
            return False
        rm_idx = self.index[val]    # index of the value to be removed
        last_val = self.val[-1]     # last value in the list
        self.val[rm_idx] = last_val # replace the value to be removed with the last value
        self.index[last_val] = rm_idx # update the index of the last value
        self.val.pop()            # remove the last value
        del self.index[val]       # remove the value from the index
        return True


        
    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.val)
        

# 測試程式碼
commands = ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
values = [[], [1], [2], [2], [], [1], [2], []]

# 初始化 RandomizedSet 對象
obj = RandomizedSet()
outputs = []

for command, value in zip(commands, values):
    if command == "RandomizedSet":
        obj = RandomizedSet()
        outputs.append(None)
    elif command == "insert":
        result = obj.insert(value[0])
        outputs.append(result)
    elif command == "remove":
        result = obj.remove(value[0])
        outputs.append(result)
    elif command == "getRandom":
        result = obj.getRandom()
        outputs.append(result)

print(outputs)