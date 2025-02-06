class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        h = 0
        for i in range(len(citations)):
            print("i + 1 =", i+1, "citations[i]=", citations[i])
            if i+1 <= citations[i]:
                h = i+1
            else:
                break
        return h
        
citations = [3,0,6,1,5]
print(Solution().hIndex(citations))  # Output: 3