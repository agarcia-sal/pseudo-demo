class Solution:
    def maxOperations(self, s: str) -> int:
        totalOps = 0
        oneCount = 0
        position = 0
        while position < len(s):
            currentChar = s[position]
            if currentChar == '1':
                oneCount += 1
            else:
                if position > 0 and s[position - 1] == '1':
                    totalOps += oneCount
            position += 1
        result = totalOps
        return result