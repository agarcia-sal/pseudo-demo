from typing import List

class Solution:
    def sumDigitDifferences(self, numbers: List[str]) -> int:
        def digit_difference(x: str, y: str) -> int:
            mismatchCount = 0
            for i in range(len(x)):
                if x[i] != y[i]:
                    mismatchCount += 1
            return mismatchCount

        aggregateSum = 0
        lengthNums = len(numbers)
        for outerIdx in range(lengthNums - 1):
            for innerIdx in range(outerIdx + 1, lengthNums):
                aggregateSum += digit_difference(numbers[outerIdx], numbers[innerIdx])
        return aggregateSum