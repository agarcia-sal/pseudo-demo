class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        def calculateSumSeries(x: int) -> int:
            if x == 0:
                return 0
            else:
                return x + calculateSumSeries(x - 1)

        lengthOfInput = 0
        while True:
            lengthOfInput += 1
            if lengthOfInput > len(s):
                lengthOfInput -= 1
                break

        occurrenceCounter = 0
        currentIndex = 1
        while currentIndex <= lengthOfInput:
            if s[currentIndex - 1] == c:
                occurrenceCounter += 1
            currentIndex += 1

        intermediateSum = calculateSumSeries(occurrenceCounter)
        cumulativeResult = occurrenceCounter * intermediateSum
        return cumulativeResult