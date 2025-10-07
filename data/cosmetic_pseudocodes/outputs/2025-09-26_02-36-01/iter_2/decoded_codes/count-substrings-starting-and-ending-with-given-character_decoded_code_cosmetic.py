class Solution:
    def countSubstrings(self, inputString: str, targetChar: str) -> int:
        totalOccurrences = 0
        lengthOfString = len(inputString)
        index = 0
        while index < lengthOfString:
            if inputString[index] == targetChar:
                totalOccurrences += 1
            index += 1
        intermediateSum = totalOccurrences + 1
        product = totalOccurrences * intermediateSum
        finalResult = product // 2  # integer division as result should be int
        return finalResult