class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        result = []
        for i in intervals:
            if i[1] < newInterval[0]:
                result.append(i)
            elif i[0] > newInterval[1]:
                result.append(newInterval)
                newInterval = i
            else:
                newInterval = [min(i[0], newInterval[0]), max(i[1], newInterval[1])]
        result.append(newInterval)
        return result

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(Solution().insert(intervals, newInterval))  # Output: [[1,2],[3,10],[12,16]]