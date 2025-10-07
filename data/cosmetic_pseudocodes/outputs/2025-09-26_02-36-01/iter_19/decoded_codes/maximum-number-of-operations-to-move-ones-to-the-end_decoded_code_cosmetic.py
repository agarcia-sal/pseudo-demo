class Solution:
    def maxOperations(self, inputString: str) -> int:
        totalResults = 0
        currentCount = 0
        position = 0
        while position < len(inputString):
            if inputString[position] == '1':
                currentCount += 1
            else:
                if position > 0 and inputString[position - 1] == '1':
                    totalResults += currentCount
            position += 1
        return totalResults