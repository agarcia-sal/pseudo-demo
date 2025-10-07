from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        frequencyMap = Counter(s)
        oddCountSum = 0
        evenCountSum = 0

        values = list(frequencyMap.values())
        index = 0
        while index < len(values):
            currentValue = values[index]
            remainder = currentValue - 2 * (currentValue // 2)
            if remainder == 1:
                oddCountSum += 1
            else:
                if remainder != 1 and currentValue != 0:
                    evenCountSum += 2
            index += 1

        totalResult = oddCountSum + evenCountSum
        return totalResult